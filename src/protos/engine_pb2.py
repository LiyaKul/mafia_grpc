# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engine.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x65ngine.proto\"7\n\x0bJoinRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"6\n\x0cJoinResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"8\n\x0cLeaveRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"+\n\rLeaveResponse\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"=\n\x11GetPlayersRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"1\n\x12GetPlayersResponse\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x01(\t\"8\n\x0cStartRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"\x8c\x01\n\rStartResponse\x12\x0f\n\x07started\x18\x01 \x01(\x08\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x11\n\x04text\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07players\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06mafias\x18\x05 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_textB\n\n\x08_playersB\t\n\x07_mafias\"7\n\x0bInfoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"l\n\x0cInfoResponse\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10\x64\x65\x61\x64_player_name\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_textB\x13\n\x11_dead_player_name\"J\n\x0bKillRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tkill_name\x18\x02 \x01(\t\x12\x11\n\x04text\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\":\n\x0cKillResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"L\n\x0c\x43heckRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncheck_name\x18\x02 \x01(\t\x12\x11\n\x04text\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"W\n\rCheckResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x11\n\x04role\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04text\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_roleB\x07\n\x05_text\"J\n\x0bVoteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tvote_name\x18\x02 \x01(\t\x12\x11\n\x04text\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\":\n\x0cVoteResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"9\n\rEndDayRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"o\n\x0e\x45ndDayResponse\x12\r\n\x05\x65nded\x18\x01 \x01(\x08\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10\x64\x65\x61\x64_player_name\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_textB\x13\n\x11_dead_player_name\";\n\x0f\x45ndNightRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"q\n\x10\x45ndNightResponse\x12\r\n\x05\x65nded\x18\x01 \x01(\x08\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10\x64\x65\x61\x64_player_name\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_textB\x13\n\x11_dead_player_name\":\n\x0ePublishRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"=\n\x0fPublishResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text2\x84\x04\n\x0c\x45ngineServer\x12%\n\x04Join\x12\x0c.JoinRequest\x1a\r.JoinResponse\"\x00\x12(\n\x05Leave\x12\r.LeaveRequest\x1a\x0e.LeaveResponse\"\x00\x12\x37\n\nGetPlayers\x12\x12.GetPlayersRequest\x1a\x13.GetPlayersResponse\"\x00\x12(\n\x05Start\x12\r.StartRequest\x1a\x0e.StartResponse\"\x00\x12%\n\x04Kill\x12\x0c.KillRequest\x1a\r.KillResponse\"\x00\x12(\n\x05\x43heck\x12\r.CheckRequest\x1a\x0e.CheckResponse\"\x00\x12%\n\x04Vote\x12\x0c.VoteRequest\x1a\r.VoteResponse\"\x00\x12+\n\x06\x45ndDay\x12\x0e.EndDayRequest\x1a\x0f.EndDayResponse\"\x00\x12\x31\n\x08\x45ndNight\x12\x10.EndNightRequest\x1a\x11.EndNightResponse\"\x00\x12;\n\x14PublishSheriffChecks\x12\x0f.PublishRequest\x1a\x10.PublishResponse\"\x00\x12+\n\x08GameInfo\x12\x0c.InfoRequest\x1a\r.InfoResponse\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'engine_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _JOINREQUEST._serialized_start=16
  _JOINREQUEST._serialized_end=71
  _JOINRESPONSE._serialized_start=73
  _JOINRESPONSE._serialized_end=127
  _LEAVEREQUEST._serialized_start=129
  _LEAVEREQUEST._serialized_end=185
  _LEAVERESPONSE._serialized_start=187
  _LEAVERESPONSE._serialized_end=230
  _GETPLAYERSREQUEST._serialized_start=232
  _GETPLAYERSREQUEST._serialized_end=293
  _GETPLAYERSRESPONSE._serialized_start=295
  _GETPLAYERSRESPONSE._serialized_end=344
  _STARTREQUEST._serialized_start=346
  _STARTREQUEST._serialized_end=402
  _STARTRESPONSE._serialized_start=405
  _STARTRESPONSE._serialized_end=545
  _INFOREQUEST._serialized_start=547
  _INFOREQUEST._serialized_end=602
  _INFORESPONSE._serialized_start=604
  _INFORESPONSE._serialized_end=712
  _KILLREQUEST._serialized_start=714
  _KILLREQUEST._serialized_end=788
  _KILLRESPONSE._serialized_start=790
  _KILLRESPONSE._serialized_end=848
  _CHECKREQUEST._serialized_start=850
  _CHECKREQUEST._serialized_end=926
  _CHECKRESPONSE._serialized_start=928
  _CHECKRESPONSE._serialized_end=1015
  _VOTEREQUEST._serialized_start=1017
  _VOTEREQUEST._serialized_end=1091
  _VOTERESPONSE._serialized_start=1093
  _VOTERESPONSE._serialized_end=1151
  _ENDDAYREQUEST._serialized_start=1153
  _ENDDAYREQUEST._serialized_end=1210
  _ENDDAYRESPONSE._serialized_start=1212
  _ENDDAYRESPONSE._serialized_end=1323
  _ENDNIGHTREQUEST._serialized_start=1325
  _ENDNIGHTREQUEST._serialized_end=1384
  _ENDNIGHTRESPONSE._serialized_start=1386
  _ENDNIGHTRESPONSE._serialized_end=1499
  _PUBLISHREQUEST._serialized_start=1501
  _PUBLISHREQUEST._serialized_end=1559
  _PUBLISHRESPONSE._serialized_start=1561
  _PUBLISHRESPONSE._serialized_end=1622
  _ENGINESERVER._serialized_start=1625
  _ENGINESERVER._serialized_end=2141
# @@protoc_insertion_point(module_scope)