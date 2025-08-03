# Upgrades

This document describes version specific upgrade instructions.

!!! Note

    Always backup your database before performing an upgrade to next Papermerge version

## 3.5.3 (not yet released)

When migration from `3.5.2` to `3.5.3` make sure that you don't have in database table `users` entries with `home_folder_id` or `inbox_folder_id` columns set to NULL - in such case migration will fail. 

Though, it was possible before 3.5.3 under certain circumstances, to create users with either one or both of these two columns set to NULL, it is very unlikely that this case is relevant for you.
In case you have some - please delete these entries (`DELETE users WHERE home_folder_id IS NULL OR inbox_folder_id IS NULL`)
No worries about deleting user entity with NULL value for `home_folder_id` or `home_folder_id` as such entities are stale anyway - they have no documents associated and no login is possible. 