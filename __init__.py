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


class BouddhaSkill(MycroftSkill):

    def __init__(self):
        super(BouddhaSkill, self).__init__(name="BouddhaSkill")

    def initialize(self):
        tell_me_a_quote_from_bouddha_intent = IntentBuilder("TellMeAQuoteFromBouddha")\
            .require("TellMeAQuoteFromBouddhaKeyword").build()
        self.register_intent(tell_me_a_quote_from_bouddha_intent,
                             self.handle_tell_me_a_quote_from_bouddha_intent)

        

    def handle_when_were_you_born_intent(self, message):
        self.speak_dialog("when.was.i.born")

    def handle_where_were_you_born_intent(self, message):
        self.speak_dialog("where.was.i.born")

    def handle_who_made_you_intent(self, message):
        self.speak_dialog("who.made.me")

    def handle_who_are_you_intent(self, message):
        name = self.config_core.get("listener", {}).get("wake_word",
                                                        "mycroft")
        name = name.lower().replace("hey ", "")
        self.speak_dialog("who.am.i", {"name": name})

    def handle_what_are_you_intent(self, message):
        self.speak_dialog("what.am.i")

    def stop(self):
        pass


def create_skill():
    return PersonalSkill()
