# SideBarPro

## Description

SideBarPro is a powerful extension for Sublime Text that enhances the sidebar menu. Notable features include "move to trash" for file deletion, a clipboard manager, and automatic closing, renaming/moving, and restoring of files affected by rename/move commands.

**A fork from [titoBouzout/SideBarEnhancements](https://github.com/titoBouzout/SideBarEnhancements)**, this project builds upon and improves the original functionalities for an even better user experience.

## Default Menu Items

To remove the default Sublime Text sidebar menu items, create two empty files in "Preferences -> Browse Packages":

-   `Default/Side Bar Mount Point.sublime-menu`
-   `Default/Side Bar.sublime-menu`

## External Libraries

SideBarPro relies on several external libraries to provide its features:

-   **desktop**: Allows opening files with system handlers. See: [desktop on PyPI](http://pypi.python.org/pypi/desktop)
-   **send2trash**: Enables sending files to the trash instead of permanently deleting them. See: [Send2Trash on PyPI](http://pypi.python.org/pypi/Send2Trash)
-   **hurry.filesize**: Formats file sizes in a human-readable way. See: [hurry.filesize on PyPI](http://pypi.python.org/pypi/hurry.filesize/)
-   **Edit.py**: ST2/3 Edit Abstraction. See: [Edit.py on Sublime Text Forum](http://www.sublimetext.com/forum/viewtopic.php?f=6&t=12551)

## License

"None are so hopelessly enslaved as those who falsely believe they are free."
Johann Wolfgang von Goethe

Copyright (C) 2011-2024 Tito Bouzout

This license applies to all the files inside this program unless noted different
for some files or portions of code inside these files.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation. <http://www.gnu.org/licenses/gpl.html>

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/gpl.html>
