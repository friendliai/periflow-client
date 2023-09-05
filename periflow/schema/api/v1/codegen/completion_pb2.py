# Copyright (c) 2022-present, FriendliAI Inc. All rights reserved.

# pylint: disable-all

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: completion.proto
"""Generated protocol buffer code."""
from __future__ import annotations

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10\x63ompletion.proto\x12\x04orca"\xdd\x0c\n\x14V1CompletionsRequest\x12\x13\n\x06stream\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x13\n\x06prompt\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x0e\n\x06tokens\x18\x04 \x03(\x05\x12!\n\x14timeout_microseconds\x18\x05 \x01(\x05H\x02\x88\x01\x01\x12\x17\n\nmax_tokens\x18\x06 \x01(\x05H\x03\x88\x01\x01\x12\x1d\n\x10max_total_tokens\x18\x07 \x01(\x05H\x04\x88\x01\x01\x12\x17\n\nmin_tokens\x18\x08 \x01(\x05H\x05\x88\x01\x01\x12\x1d\n\x10min_total_tokens\x18\t \x01(\x05H\x06\x88\x01\x01\x12\x0e\n\x01n\x18\n \x01(\x05H\x07\x88\x01\x01\x12\x16\n\tnum_beams\x18\x0b \x01(\x05H\x08\x88\x01\x01\x12\x1b\n\x0elength_penalty\x18\x0c \x01(\x02H\t\x88\x01\x01\x12\x1b\n\x0e\x65\x61rly_stopping\x18\x0f \x01(\x08H\n\x88\x01\x01\x12\x1c\n\x0fno_repeat_ngram\x18\x11 \x01(\x05H\x0b\x88\x01\x01\x12$\n\x17\x65ncoder_no_repeat_ngram\x18\x12 \x01(\x05H\x0c\x88\x01\x01\x12\x1f\n\x12repetition_penalty\x18\x13 \x01(\x02H\r\x88\x01\x01\x12\'\n\x1a\x65ncoder_repetition_penalty\x18" \x01(\x02H\x0e\x88\x01\x01\x12\x18\n\x0btemperature\x18\x14 \x01(\x02H\x0f\x88\x01\x01\x12\x12\n\x05top_k\x18\x15 \x01(\x05H\x10\x88\x01\x01\x12\x12\n\x05top_p\x18\x16 \x01(\x02H\x11\x88\x01\x01\x12\x0c\n\x04stop\x18\x17 \x03(\t\x12=\n\x0bstop_tokens\x18\x18 \x03(\x0b\x32(.orca.V1CompletionsRequest.TokenSequence\x12\x0c\n\x04seed\x18\x1a \x03(\x04\x12\x1e\n\x16token_index_to_replace\x18\x1b \x03(\x05\x12\x1c\n\x14\x65mbedding_to_replace\x18\x1c \x03(\x02\x12H\n\x10\x62\x65\x61m_search_type\x18\x1d \x01(\x0e\x32).orca.V1CompletionsRequest.BeamSearchTypeH\x12\x88\x01\x01\x12*\n\x1d\x62\x65\x61m_compat_pre_normalization\x18\x1e \x01(\x08H\x13\x88\x01\x01\x12.\n!beam_compat_no_post_normalization\x18\x1f \x01(\x08H\x14\x88\x01\x01\x12\x11\n\tbad_words\x18  \x03(\t\x12\x41\n\x0f\x62\x61\x64_word_tokens\x18! \x03(\x0b\x32(.orca.V1CompletionsRequest.TokenSequence\x12"\n\x15include_output_logits\x18/ \x01(\x08H\x15\x88\x01\x01\x12$\n\x17include_output_logprobs\x18\x32 \x01(\x08H\x16\x88\x01\x01\x12\x1c\n\x14\x66orced_output_tokens\x18\x33 \x03(\x05\x12\x11\n\teos_token\x18. \x03(\x05\x1a\x1f\n\rTokenSequence\x12\x0e\n\x06tokens\x18\x01 \x03(\x05"G\n\x0e\x42\x65\x61mSearchType\x12\x11\n\rDETERMINISTIC\x10\x00\x12\x0e\n\nSTOCHASTIC\x10\x01\x12\x12\n\x0eNAIVE_SAMPLING\x10\x02\x42\t\n\x07_streamB\t\n\x07_promptB\x17\n\x15_timeout_microsecondsB\r\n\x0b_max_tokensB\x13\n\x11_max_total_tokensB\r\n\x0b_min_tokensB\x13\n\x11_min_total_tokensB\x04\n\x02_nB\x0c\n\n_num_beamsB\x11\n\x0f_length_penaltyB\x11\n\x0f_early_stoppingB\x12\n\x10_no_repeat_ngramB\x1a\n\x18_encoder_no_repeat_ngramB\x15\n\x13_repetition_penaltyB\x1d\n\x1b_encoder_repetition_penaltyB\x0e\n\x0c_temperatureB\x08\n\x06_top_kB\x08\n\x06_top_pB\x13\n\x11_beam_search_typeB \n\x1e_beam_compat_pre_normalizationB$\n"_beam_compat_no_post_normalizationB\x18\n\x16_include_output_logitsB\x1a\n\x18_include_output_logprobs"3\n\x11V1TokenizeRequest\x12\x13\n\x06prompt\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_prompt"%\n\x13V1DetokenizeRequest\x12\x0e\n\x06tokens\x18\x02 \x03(\x05\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "completion_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_V1COMPLETIONSREQUEST"]._serialized_start = 27
    _globals["_V1COMPLETIONSREQUEST"]._serialized_end = 1656
    _globals["_V1COMPLETIONSREQUEST_TOKENSEQUENCE"]._serialized_start = 1090
    _globals["_V1COMPLETIONSREQUEST_TOKENSEQUENCE"]._serialized_end = 1121
    _globals["_V1COMPLETIONSREQUEST_BEAMSEARCHTYPE"]._serialized_start = 1123
    _globals["_V1COMPLETIONSREQUEST_BEAMSEARCHTYPE"]._serialized_end = 1194
    _globals["_V1TOKENIZEREQUEST"]._serialized_start = 1658
    _globals["_V1TOKENIZEREQUEST"]._serialized_end = 1709
    _globals["_V1DETOKENIZEREQUEST"]._serialized_start = 1711
    _globals["_V1DETOKENIZEREQUEST"]._serialized_end = 1748
# @@protoc_insertion_point(module_scope)