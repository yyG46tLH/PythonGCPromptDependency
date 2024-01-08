import time
import PureCloudPlatformClientV2 as mygcp
import os
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint


def add_a_new_user(mygcp, mytoken, name, email, password):
    newuser = mygcp.CreateUser()
    newuser.name = name
    newuser.email = email
    newuser.password = password

    # instantiate UsersApi class as api_instance and then call the post_users API.
    api_instance = mygcp.UsersApi(mytoken)
    try:
        currentuser = api_instance.post_users(newuser)
        return currentuser
    except ApiException as e:
        print("Exception when calling AddUserRequest->add_user: %s\n" % e)


def delete_a_user(mygcp, mytoken, user_id):
    # instantiate UsersApi class as api_instance and then call the post_users API.
    api_instance = mygcp.UsersApi(mytoken)
    try:
        # Delete user
        api_response = api_instance.delete_user(user_id)
        # pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling DeleteUserRequest->delete_user: %s\n" % e)

def update_a_user(mygcp, mytoken, currentuser):
    updateuser = mygcp.UpdateUser()
    updateuser.name = "Tutorial User New Name"
    updateuser.version = currentuser.version

    newaddress = mygcp.Contact()
    newaddress.address = "3172222222"
    newaddress.media_type = "PHONE"
    newaddress.type = "WORK"

    updateuser.addresses = [newaddress]

    # instantiate UsersApi class as api_instance and then call the post_users API.
    api_instance = mygcp.UsersApi(mytoken)
    api_response = api_instance.patch_user(currentuser.id, updateuser)


def get_users_list(mygcp, mytoken):
    # create an instance of the API class
    api_instance = mygcp.UsersApi(mytoken)

    # int | Page size (optional) (default to 25)
    page_size = 25

    # int | Page number (optional) (default to 1)
    page_number = 1

    # list[str] | A list of user IDs to fetch by bulk (optional)
    id = ['id_example']

    # jabber_id: list[str] | A list of jabberIds to fetch by bulk (cannot be used with the \"id\" parameter) (optional)
    jabber_id = [
        'jabber_id_example']

    # str | Ascending or descending sort order (optional) (default to 'ASC')
    sort_order = 'ASC'

    # list[str] | Which fields, if any, to expand (optional)
    expand = ['expand_example']

    # str | Gets an integration presence for users instead of their defaults.
    # This parameter will only be used when presence is provided as an \"expand\".
    # When using this parameter the maximum number of users that can be returned is 100. (optional)
    integration_presence_source = 'integration_presence_source_example'

    # str | Only list users of this state (optional) (default to 'active')
    state = 'active'

    try:
        # Get the list of available users- full set
        #api_response = api_instance.get_users(page_size=page_size,page_number=page_number,id=id,jabber_id=jabber_id,sort_order=sort_order,expand=expand,integration_presence_source=integration_presence_source,state=state)
        # Get the list of available users- mandatory only.
        api_response = api_instance.get_users(page_size=page_size,page_number=page_number,sort_order=sort_order,state=state)
        # print(api_response)

        return api_response
    except ApiException as e:
        print("Exception when calling GetUsersRequest->get_users: %s\n" % e)


# This function produces id as first column in addition to two other columns specified by the caller.
def list_users_with_two_attr(api_response, first_col, second_col):
    # Convert api_response to dictionary.
    user_dictionary = api_response.to_dict()
    # Pull out the users from the dictionary.
    user_entities = user_dictionary.get('entities')
    # For every user in the user_entities
    for x in range(len(user_entities)):
        # print(user_entities[x])  # for debugging purpose only.
        entity_dict = user_entities[x]
        print('id:' + entity_dict.get('id') + ', ' + first_col + ':' + str(entity_dict.get(first_col)) + ', ' + second_col + ':' + str(entity_dict.get(second_col)))

