# Upgrades

This document describes version specific upgrade instructions.

!!! Note

    Always backup your database before performing an upgrade to next Papermerge version

## 3.5.3

When migration from `3.5.2` to `3.5.3` make sure that you don't have in database table `users` entries with `home_folder_id` or `inbox_folder_id` columns set to NULL - in such case migration will fail.

Though it was possible before 3.5.3 under certain circumstances to create users with either one or both of these two columns set to NULL, it is very unlikely that this case is relevant for you.
In case you have some - please delete these entries (`DELETE users WHERE home_folder_id IS NULL OR inbox_folder_id IS NULL`)
No worries about deleting user entity with NULL value for `home_folder_id` or `home_folder_id` as such entities are stale anyway - they have no documents associated and no login is possible.


## 3.6 (not yet released)

### Audit Feature Migration (v3.6)

Starting with **version 3.6**, Papermerge introduces the **Audit feature**, which records *who did what and when*.
This affects almost all database tables, which now include audit columns:

* `created_at`
* `created_by`
* `updated_at`
* `updated_by`

There are couple more, but they are irrelevant here.
The most critical change:

👉 The `users`, `groups`, `roles`, `custom_fields`, `document_types`, `tags`  tables **must have non-empty values for `created_by` and `updated_by`.**

Following steps describe how to update `users` table only. You **need to repeat** these steps for all tables
that have `created_by` and `updated_by` columns:

  * `groups`
  * `roles`
  * `custom_fields`
  * `document_types`
  * `tags`

---

#### How to Fix Existing `users` Rows

If you are upgrading, you must manually update `users.created_by` and `users.updated_by` to valid user IDs (for example, your administrator user).

⚠️ **Important:** You must **disable** the trigger `set_created_by_updated_by_trigger_users` (
   set_created_by_updated_by_trigger_**groups**, set_created_by_updated_by_trigger_**custom_fields** etc)
before updating, otherwise the update will not work.

---

#### Step 1: Find your admin’s user ID

```sql
SELECT id, username, updated_by, created_by FROM users;

-- Example output:
-- 49e78737-7c6e-410f-ae27-315b04bdec69 | admin | <empty> | <empty>
```

Copy your admin user’s `id`.

---

#### Step 2: Disable the trigger

```sql
ALTER TABLE users DISABLE TRIGGER set_created_by_updated_by_trigger_users;
```

"...DISABLE TRIGGER set_created_by_updated_by_trigger_**groups**;", "...DISABLE TRIGGER set_created_by_updated_by_trigger_**custom_fields**;" etc

---

#### Step 3: Update all users

```sql
UPDATE users
SET updated_by='49e78737-7c6e-410f-ae27-315b04bdec69',
    created_by='49e78737-7c6e-410f-ae27-315b04bdec69';
```

"UPDATE **groups** SET ...", "UPDATE **custom_fields** SET ..." etc

---

#### Step 4: Verify the update

```sql
SELECT id, username, updated_by, created_by FROM users;

-- Example output:
-- 49e78737-7c6e-410f-ae27-315b04bdec69 | admin | 49e78737-7c6e-410f-ae27-315b04bdec69 | 49e78737-7c6e-410f-ae27-315b04bdec69
```

"... FROM **groups**", "... FROM **custom_fields**" etc

---

#### Step 5: Re-enable the trigger

```sql
ALTER TABLE users ENABLE TRIGGER set_created_by_updated_by_trigger_users;
```

"...ENABLE TRIGGER set_created_by_updated_by_trigger_**groups**;", "...ENABLE TRIGGER set_created_by_updated_by_trigger_**custom_fields**;" etc


---

✅ Now all `users.created_by` and `users.updated_by` fields are properly set, and the audit system will function correctly.


---

