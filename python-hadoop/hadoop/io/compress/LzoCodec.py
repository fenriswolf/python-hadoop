#!/usr/bin/env python
# ========================================================================
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import lzo

from hadoop.io.InputStream import DataInputBuffer

class LzoCodec:
    hadoop_module_name = 'com.hadoop.compression.lzo'
    hadoop_class_name = 'LzoCodec'
        
    def compress(self, data):
        return lzo.compress(data, 1)

    def decompress(self, data):
        return lzo.decompress(data)

    def decompressInputStream(self, data):
        return DataInputBuffer(lzo.decompress(data))

