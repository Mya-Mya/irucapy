from mytesttool import testerfunc
import irucapy


@testerfunc
def room():
    print("Valid Room Json Text")
    valid_room_json_text =\
        '{"id":1,"code":"81263a2b-1bdd-49a4-bbc0-7a59639fcb28","name":"Mya-Mya Room","note":"This room does not exist.","statuses":["A","B"],"created_at":"2021-10-01T01:00:00.000Z","updated_at":"2022-04-01T16:00:00.000Z","status_updated_at":"2022-05-01T22:00:00.000Z"}'
    obj = irucapy.api.room.from_json_maybe(valid_room_json_text)
    assert obj == irucapy.api.room.Room(
        id=1,
        code="81263a2b-1bdd-49a4-bbc0-7a59639fcb28",
        name="Mya-Mya Room",
        note="This room does not exist.",
        statuses=["A", "B"],
        created_at="2021-10-01T01:00:00.000Z",
        updated_at="2022-04-01T16:00:00.000Z",
        status_updated_at="2022-05-01T22:00:00.000Z"
    )

    print("Insufficient Room Json Text")
    insufficient_room_json_text =\
        '{"code":"81263a2b-1bdd-49a4-bbc0-7a59639fcb28","name":"Mya-Mya Room","note":"This room does not exist.","statuses":["A","B"],"created_at":"2021-10-01T01:00:00.000Z","updated_at":"2022-04-01T16:00:00.000Z","status_updated_at":"2022-05-01T22:00:00.000Z"}'
    obj = irucapy.api.room.from_json_maybe(insufficient_room_json_text)
    assert obj is None

    print("Excessive Room Json Text")
    excessive_room_json_text =\
        '{"additional":"additional","id":1,"code":"81263a2b-1bdd-49a4-bbc0-7a59639fcb28","name":"Mya-Mya Room","note":"This room does not exist.","statuses":["A","B"],"created_at":"2021-10-01T01:00:00.000Z","updated_at":"2022-04-01T16:00:00.000Z","status_updated_at":"2022-05-01T22:00:00.000Z"}'
    obj = irucapy.api.room.from_json_maybe(excessive_room_json_text)
    assert obj is None


@testerfunc
def member():
    print("Valid Member Json Text")
    valid_member_json_text =\
        '{"id":10000,"room_id":1,"name":"Mya-Mya","status":"B","message":"I do not exist.","created_at":"2022-02-10T03:10:00.000Z","updated_at":"2022-03-20T16:00:00.000Z","position":4}'
    obj = irucapy.api.member.from_json_maybe(valid_member_json_text)
    assert obj == irucapy.api.member.Member(
        id=10000,
        room_id=1,
        name="Mya-Mya",
        status="B",
        message="I do not exist.",
        created_at="2022-02-10T03:10:00.000Z",
        updated_at="2022-03-20T16:00:00.000Z",
        position=4
    )

    print("Insufficient Member Json Text")
    insufficient_member_json_text =\
        '{"room_id":1,"name":"Mya-Mya","status":"B","message":"I do not exist.","created_at":"2022-02-10T03:10:00.000Z","updated_at":"2022-03-20T16:00:00.000Z","position":4}'
    obj = irucapy.api.member.from_json_maybe(insufficient_member_json_text)
    assert obj is None

    print("Excessive Member Json Text")
    excessive_member_json_text =\
        '{"additional":"additional","id":10000,"room_id":1,"name":"Mya-Mya","status":"B","message":"I do not exist.","created_at":"2022-02-10T03:10:00.000Z","updated_at":"2022-03-20T16:00:00.000Z","position":4}'
    obj = irucapy.api.member.from_json_maybe(excessive_member_json_text)
    assert obj is None


@testerfunc
def members():
    print("Valid Members Json Text")
    valid_members_json_text =\
        '['\
        '{"id":10000,"room_id":1,"name":"Mya-Mya","status":"B","message":"I do not exist.","created_at":"2022-02-10T03:10:00.000Z","updated_at":"2022-03-20T16:00:00.000Z","position":4},'\
        '{"id":10001,"room_id":1,"name":"Nya-Nya","status":"A","message":"I do not not exist.","created_at":"2022-02-10T04:10:00.000Z","updated_at":"2022-03-20T17:00:00.000Z","position":5},'\
        '{"id":10002,"room_id":1,"name":"Kya-Kya","status":"A","message":"I do not not not exist.","created_at":"2022-02-10T04:12:00.000Z","updated_at":"2022-03-20T18:00:00.000Z","position":6}'\
        ']'
    obj = irucapy.api.members.from_json_maybe(valid_members_json_text)
    assert obj == [
        irucapy.api.member.Member(
            id=10000,
            room_id=1,
            name="Mya-Mya",
            status="B",
            message="I do not exist.",
            created_at="2022-02-10T03:10:00.000Z",
            updated_at="2022-03-20T16:00:00.000Z",
            position=4
        ),
        irucapy.api.member.Member(
            id=10001,
            room_id=1,
            name="Nya-Nya",
            status="A",
            message="I do not not exist.",
            created_at="2022-02-10T04:10:00.000Z",
            updated_at="2022-03-20T17:00:00.000Z",
            position=5
        ),
        irucapy.api.member.Member(
            id=10002,
            room_id=1,
            name="Kya-Kya",
            status="A",
            message="I do not not not exist.",
            created_at="2022-02-10T04:12:00.000Z",
            updated_at="2022-03-20T18:00:00.000Z",
            position=6
        )
    ]

room()
member()
members()