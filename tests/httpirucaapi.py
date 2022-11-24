from mytesttool import testerfunc
import irucapy


@testerfunc
def get_room_info():
    room = api.get_room_info(room_code)
    print(room)


@testerfunc
def get_room_members():
    members = api.get_room_members(room_code)
    print(members)


@testerfunc
def get_room_member():
    member_id = int(input("MEMBER ID: "))
    member = api.get_room_member(room_code, member_id)
    print(member)


@testerfunc
def update_room_member():
    member_id = int(input("MEMBER ID: "))
    status = input("STATUS: ")
    message_input = input("MESSAGE(none for None): ")
    message = None if message_input=="none" else message_input
    param = irucapy.memberupdate.MemberUpdateParam(status, None, message)
    api.update_room_member(room_code, member_id, param)


room_code = input("ROOM-CODE: ")
api = irucapy.HTTPIrucaAPI()
get_room_members()
update_room_member()
