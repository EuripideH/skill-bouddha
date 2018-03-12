# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger


logger = getLogger(__name__)


class BuddhaSkill(MycroftSkill):

    def __init__(self):
        super(BuddhaSkill, self).__init__(name="BuddhaSkill")

    def initialize(self):
        tell_me_a_quote_from_buddha_intent = IntentBuilder("TellMeAQuoteFromBuddha")\
            .require("TellMeAQuoteFromBuddhaKeyword").build()
        self.register_intent(tell_me_a_quote_from_buddha_intent,
                             self.handle_tell_me_a_quote_from_buddha_intent)

        
    def handle_ tell_me_a_quote_from_buddha_intent(self, message):
        self.speak_dialog("buddha.quotes.born")

    
  def stop(self):
        pass


def create_skill():
    return BuddhaSkill()
