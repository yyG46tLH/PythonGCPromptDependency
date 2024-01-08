# Import modules
import PureCloudPlatformClientV2 as mygcp
import os
import time

# Import Genesys Cloud Center modules/libraries
from GCCInit import *
from GCCFileLocator import *
from GCCLogger import *
from GCCUserPrompts import *

if __name__ == '__main__':
    # Initiate logging
    app_log_file = os.environ['GENESYS_CLOUD_SDK_LOG'] + '\\UPDL.log'
    upl_logger = init_logger(app_log_file, 'DEBUG')
    upl_logger.info('UserPrompts started...')

    user_goahead = input('List User Prompts and Dependencies? (y/q): ')

    if user_goahead.lower() == 'y':
        flow_type_list_filename = os.environ['GENESYS_CLOUD_SDK_LOG'] + '\\FlowTypeList.xlsx'

        if check_file_exist(flow_type_list_filename):
            log_msg = 'Reading FlowTypeList.xlsx from ' + os.environ['GENESYS_CLOUD_SDK_LOG']
            upl_logger.info(log_msg)
            # Store flow types in a list, flow_type_list
            flow_type_list = read_flow_types(flow_type_list_filename)
            print(f'Found flow types: {flow_type_list}')
        else:
            log_msg = flow_type_list_filename + ' does not exist. Please place or create it and run this program again.'
            upl_logger.error(log_msg)
            print(log_msg)
            raise SystemExit(log_msg)

        output_template_filename = os.environ['GENESYS_CLOUD_SDK_LOG'] + '\\OutputTemplate.xlsx'

        if check_file_exist(output_template_filename):
            log_msg = 'Initializing OutputTemplate.xlsx from ' + os.environ['GENESYS_CLOUD_SDK_LOG']
            upl_logger.info(log_msg)
            # Store flow types in a list, flow_type_list
            output_wb, output_sheet = prepare_output_xlsx(output_template_filename)
        else:
            log_msg = output_template_filename + \
                      ' does not exist. Please place or create it and run this program again.'
            upl_logger.error(log_msg)
            print(log_msg)
            raise SystemExit(log_msg)

        log_msg = 'Initializing API object'
        upl_logger.info(log_msg)

        # Initialize mygcp for use
        mygcp, mytoken = initialize_my_gcp(mygcp)
        # create an instance of the API class
        api_instance = mygcp.ArchitectApi(mytoken)

        log_msg = 'Exporting User Prompts and Dependencies list.'
        upl_logger.info(log_msg)

        # Execute API to get list of user prompts.
        total_pg_count = get_all_user_prompt_pg_count(api_instance, upl_logger)

        # Extract user prompt ids from all pages in app_response.
        user_prompt_name_list = retrieve_user_prompt_names(total_pg_count, api_instance, upl_logger)

        # output_xlsx_row_start = output_sheet.max_row + 1

        # Loop through user prompt names and flow types.
        # Per user prompt name,
        for name in user_prompt_name_list:
            next_user_prompt_name = name
            # log_msg = 'Processing ' + next_user_prompt_name
            # upl_logger.info(log_msg)
            # print(log_msg)

            # Per flow type
            for flowtype in flow_type_list:
                next_flow_type = flowtype
                # log_msg = 'Processing ' + next_flow_type
                # upl_logger.info(log_msg)
                # print(log_msg)

                # Get number of resulting page for dependency resource.
                dependency_pg_count = get_all_up_dependencies_pg_count(api_instance,
                                                                       next_user_prompt_name,
                                                                       next_flow_type, upl_logger)
                log_msg = str(dependency_pg_count) + ' pages found for ' \
                          + next_flow_type + ' using ' + next_user_prompt_name
                upl_logger.info(log_msg)
                if dependency_pg_count > 0:
                    output_wb, output_sheet = retrieve_dependencies(
                        output_wb,
                        output_sheet,
                        dependency_pg_count,
                        api_instance,
                        next_user_prompt_name,
                        next_flow_type,
                        upl_logger)
            # print('Sleeping...')
            time.sleep(1)  # Don't over stress API

    input('Processing complete. Press ENTER to exit ')
    log_msg = 'Exiting UserPromptListing via user input.'
    upl_logger.info(log_msg)

    # Save output spreadsheet
    new_xlsx_name = os.environ['GENESYS_CLOUD_SDK_LOG'] + '\\UPDL_Output_' + str(time.time()) + '.xlsx'
    print(f'Saving {new_xlsx_name}')
    output_wb.save(new_xlsx_name)

    