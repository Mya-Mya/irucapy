from mytesttool import testerfunc
import irucapy

@testerfunc
def get_room_info():
    room = api.get_room_info(room_code)
    print(room)

room_code = input("ROOM-CODE: ")
api = irucapy.api.httpirucaapi.HTTPIrucaAPI()
get_room_member()