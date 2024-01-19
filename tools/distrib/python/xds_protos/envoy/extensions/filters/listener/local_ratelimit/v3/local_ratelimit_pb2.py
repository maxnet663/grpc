# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/listener/local_ratelimit/v3/local_ratelimit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.type.v3 import token_bucket_pb2 as envoy_dot_type_dot_v3_dot_token__bucket__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJenvoy/extensions/filters/listener/local_ratelimit/v3/local_ratelimit.proto\x12\x34\x65nvoy.extensions.filters.listener.local_ratelimit.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a envoy/type/v3/token_bucket.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xad\x01\n\x0eLocalRateLimit\x12\x1c\n\x0bstat_prefix\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12:\n\x0ctoken_bucket\x18\x02 \x01(\x0b\x32\x1a.envoy.type.v3.TokenBucketB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x41\n\x0fruntime_enabled\x18\x03 \x01(\x0b\x32(.envoy.config.core.v3.RuntimeFeatureFlagB\xd2\x01\nBio.envoyproxy.envoy.extensions.filters.listener.local_ratelimit.v3B\x13LocalRatelimitProtoP\x01Zmgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/local_ratelimit/v3;local_ratelimitv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.extensions.filters.listener.local_ratelimit.v3.local_ratelimit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nBio.envoyproxy.envoy.extensions.filters.listener.local_ratelimit.v3B\023LocalRatelimitProtoP\001Zmgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/local_ratelimit/v3;local_ratelimitv3\272\200\310\321\006\002\020\002'
  _LOCALRATELIMIT.fields_by_name['stat_prefix']._options = None
  _LOCALRATELIMIT.fields_by_name['stat_prefix']._serialized_options = b'\372B\004r\002\020\001'
  _LOCALRATELIMIT.fields_by_name['token_bucket']._options = None
  _LOCALRATELIMIT.fields_by_name['token_bucket']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_LOCALRATELIMIT']._serialized_start=256
  _globals['_LOCALRATELIMIT']._serialized_end=429
# @@protoc_insertion_point(module_scope)