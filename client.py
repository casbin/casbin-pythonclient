# Copyright 2017 The casbin Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import urllib2


def request_enforcement(tenant, sub, obj, act):
    url = 'http://localhost:8080/decision'
    values = {"Tenant": tenant, "Sub": sub, "Obj": obj, "Act": act}
    params = str(values)
    params = params.replace("'", '"')
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    response = urllib2.urlopen(req)
    print response.read()

if __name__ == "__main__":
    request_enforcement("tenant1", "admin", "res1", "GET")
