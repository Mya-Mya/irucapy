from mytesttool import testerfunc
import irucapy


@testerfunc
def get_room_info():
    room = client.get_room_info()
    print(room)


@testerfunc
def get_room_members():
    members = client.get_room_members()
    print(members)


@testerfunc
def get_room_member():
    member_id = int(input("MEMBER ID: "))
    member = client.get_room_member(member_id)
    print(member)


@testerfunc
def update_room_member():
    member_id = int(input("MEMBER ID: "))
    status = input("STATUS: ")
    client.update_room_member(member_id, status, message="message")


room_code = input("ROOM-CODE: ")
client = irucapy.IrucaClient(
    room_code, irucapy.HTTPIrucaAPI())
# get_room_info()
# get_room_members()
# get_room_member()
update_room_member()
