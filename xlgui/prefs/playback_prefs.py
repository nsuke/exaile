# Copyright (C) 2006 Adam Olsen
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 1, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from xlgui.prefs import widgets
from xl import xdg
from xlgui import commondialogs

name = "Playback"
glade = xdg.get_data_path('glade/playback_prefs_pane.glade')

class ResumePreference(widgets.CheckPrefsItem):
    default = True
    name = 'player/resume_playback'

class PausedPreference(widgets.CheckPrefsItem):
    default = False
    name = 'player/resume_paused' 

class UserFadeTogglePreference(widgets.CheckPrefsItem):
    default = False
    name = 'player/user_fade_enabled' 

class UserFadeDurationPreference(widgets.SpinPrefsItem):
    default = 1000
    name = 'player/user_fade'

class CrossfadingPreference(widgets.CheckPrefsItem):
    default = False
    name = 'player/crossfading'

class CrossfadeDurationPreference(widgets.SpinPrefsItem):
    default = 1000
    name = 'player/crossfade_duration'

