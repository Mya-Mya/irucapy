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

room_code = input("ROOM-CODE: ")
api = irucapy.api.httpirucaapi.HTTPIrucaAPI()
get_room_member()