# get All Permission

**GET** `{{url}}/api/permission/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### get All Permission

**Request:** `GET` `{{url}}/api/permission/`

**Response:** `200 OK`

```json
{
    "success": true,
    "data": [
        {
            "actiontype": [
                {
                    "name": "Can add action type",
                    "codename": "add_actiontype"
                },
                {
                    "name": "Can change action type",
                    "codename": "change_actiontype"
                },
                {
                    "name": "Can delete action type",
                    "codename": "delete_actiontype"
                },
                {
                    "name": "Can view action type",
                    "codename": "view_actiontype"
                }
            ]
        },
        {
            "activitylog": [
                {
                    "name": "Can add activity log",
                    "codename": "add_activitylog"
                },
                {
                    "name": "Can change activity log",
                    "codename": "change_activitylog"
                },
                {
                    "name": "Can delete activity log",
                    "codename": "delete_activitylog"
                },
                {
                    "name": "Can view activity log",
                    "codename": "view_activitylog"
                }
            ]
        },
        {
            "authenticationlog": [
                {
                    "name": "Can add user_login_activity",
                    "codename": "add_authenticationlog"
                },
                {
                    "name": "Can change user_login_activity",
                    "codename": "change_authenticationlog"
                },
                {
                    "name": "Can delete user_login_activity",
                    "codename": "delete_authenticationlog"
                },
                {
                    "name": "Can view user_login_activity",
                    "codename": "view_authenticationlog"
                }
            ]
        },
        {
            "logentry": [
                {
                    "name": "Can add log entry",
                    "codename": "add_logentry"
                },
                {
                    "name": "Can change log entry",
                    "codename": "change_logentry"
                },
                {
                    "name": "Can delete log entry",
                    "codename": "delete_logentry"
                },
                {
                    "name": "Can view log entry",
                    "codename": "view_logentry"
                }
            ]
        },
        {
            "currencymodel": [
                {
                    "name": "Can add currency model",
                    "codename": "add_currencymodel"
                },
                {
                    "name": "Can change currency model",
                    "codename": "change_currencymodel"
                },
                {
                    "name": "Can delete currency model",
                    "codename": "delete_currencymodel"
                },
                {
                    "name": "Can view currency model",
                    "codename": "view_currencymodel"
                }
            ]
        },
        {
            "datasource": [
                {
                    "name": "Can add data source",
                    "codename": "add_datasource"
                },
                {
                    "name": "Can change data source",
                    "codename": "change_datasource"
                },
                {
                    "name": "Can delete data source",
                    "codename": "delete_datasource"
                },
                {
                    "name": "Can view data source",
                    "codename": "view_datasource"
                }
            ]
        },
        {
            "group": [
                {
                    "name": "Can add group",
                    "codename": "add_group"
                },
                {
                    "name": "Can change group",
                    "codename": "change_group"
                },
                {
                    "name": "Can delete group",
                    "codename": "delete_group"
                },
                {
                    "name": "Can view group",
                    "codename": "view_group"
                }
            ]
        },
        {
            "permission": [
                {
                    "name": "Can add permission",
                    "codename": "add_permission"
                },
                {
                    "name": "Can change permission",
                    "codename": "change_permission"
                },
                {
                    "name": "Can delete permission",
                    "codename": "delete_permission"
                },
                {
                    "name": "Can view permission",
                    "codename": "view_permission"
                }
            ]
        },
        {
            "contenttype": [
                {
                    "name": "Can add content type",
                    "codename": "add_contenttype"
                },
                {
                    "name": "Can change content type",
                    "codename": "change_contenttype"
                },
                {
                    "name": "Can delete content type",
                    "codename": "delete_contenttype"
                },
                {
                    "name": "Can view content type",
                    "codename": "view_contenttype"
                }
            ]
        },
        {
            "clockedschedule": [
                {
                    "name": "Can add clocked",
                    "codename": "add_clockedschedule"
                },
                {
                    "name": "Can change clocked",
                    "codename": "change_clockedschedule"
                },
                {
                    "name": "Can delete clocked",
                    "codename": "delete_clockedschedule"
                },
                {
                    "name": "Can view clocked",
                    "codename": "view_clockedschedule"
                }
            ]
        },
        {
            "crontabschedule": [
                {
                    "name": "Can add crontab",
                    "codename": "add_crontabschedule"
                },
                {
                    "name": "Can change crontab",
                    "codename": "change_crontabschedule"
                },
                {
                    "name": "Can delete crontab",
                    "codename": "delete_crontabschedule"
                },
                {
                    "name": "Can view crontab",
                    "codename": "view_crontabschedule"
                }
            ]
        },
        {
            "intervalschedule": [
                {
                    "name": "Can add interval",
                    "codename": "add_intervalschedule"
                },
                {
                    "name": "Can change interval",
                    "codename": "change_intervalschedule"
                },
                {
                    "name": "Can delete interval",
                    "codename": "delete_intervalschedule"
                },
                {
                    "name": "Can view interval",
                    "codename": "view_intervalschedule"
                }
            ]
        },
        {
            "periodictask": [
                {
                    "name": "Can add periodic task",
                    "codename": "add_periodictask"
                },
                {
                    "name": "Can change periodic task",
                    "codename": "change_periodictask"
                },
                {
                    "name": "Can delete periodic task",
                    "codename": "delete_periodictask"
                },
                {
                    "name": "Can view periodic task",
                    "codename": "view_periodictask"
                }
            ]
        },
        {
            "periodictasks": [
                {
                    "name": "Can add periodic tasks",
                    "codename": "add_periodictasks"
                },
                {
                    "name": "Can change periodic tasks",
                    "codename": "change_periodictasks"
                },
                {
                    "name": "Can delete periodic tasks",
                    "codename": "delete_periodictasks"
                },
                {
                    "name": "Can view periodic tasks",
                    "codename": "view_periodictasks"
                }
            ]
        },
        {
            "solarschedule": [
                {
                    "name": "Can add solar event",
                    "codename": "add_solarschedule"
                },
                {
                    "name": "Can change solar event",
                    "codename": "change_solarschedule"
                },
                {
                    "name": "Can delete solar event",
                    "codename": "delete_solarschedule"
                },
                {
                    "name": "Can view solar event",
                    "codename": "view_solarschedule"
                }
            ]
        },
        {
            "chordcounter": [
                {
                    "name": "Can add chord counter",
                    "codename": "add_chordcounter"
                },
                {
                    "name": "Can change chord counter",
                    "codename": "change_chordcounter"
                },
                {
                    "name": "Can delete chord counter",
                    "codename": "delete_chordcounter"
                },
                {
                    "name": "Can view chord counter",
                    "codename": "view_chordcounter"
                }
            ]
        },
        {
            "groupresult": [
                {
                    "name": "Can add group result",
                    "codename": "add_groupresult"
                },
                {
                    "name": "Can change group result",
                    "codename": "change_groupresult"
                },
                {
                    "name": "Can delete group result",
                    "codename": "delete_groupresult"
                },
                {
                    "name": "Can view group result",
                    "codename": "view_groupresult"
                }
            ]
        },
        {
            "taskresult": [
                {
                    "name": "Can add task result",
                    "codename": "add_taskresult"
                },
                {
                    "name": "Can change task result",
                    "codename": "change_taskresult"
                },
                {
                    "name": "Can delete task result",
                    "codename": "delete_taskresult"
                },
                {
                    "name": "Can view task result",
                    "codename": "view_taskresult"
                }
            ]
        },
        {
            "resetpasswordtoken": [
                {
                    "name": "Can add Password Reset Token",
                    "codename": "add_resetpasswordtoken"
                },
                {
                    "name": "Can change Password Reset Token",
                    "codename": "change_resetpasswordtoken"
                },
                {
                    "name": "Can delete Password Reset Token",
                    "codename": "delete_resetpasswordtoken"
                },
                {
                    "name": "Can view Password Reset Token",
                    "codename": "view_resetpasswordtoken"
                }
            ]
        },
        {
            "emailschedulemodel": [
                {
                    "name": "Can add email schedule model",
                    "codename": "add_emailschedulemodel"
                },
                {
                    "name": "Can change email schedule model",
                    "codename": "change_emailschedulemodel"
                },
                {
                    "name": "Can delete email schedule model",
                    "codename": "delete_emailschedulemodel"
                },
                {
                    "name": "Can view email schedule model",
                    "codename": "view_emailschedulemodel"
                }
            ]
        },
        {
            "notificationmodel": [
                {
                    "name": "Can add notification model",
                    "codename": "add_notificationmodel"
                },
                {
                    "name": "Can change notification model",
                    "codename": "change_notificationmodel"
                },
                {
                    "name": "Can delete notification model",
                    "codename": "delete_notificationmodel"
                },
                {
                    "name": "Can view notification model",
                    "codename": "view_notificationmodel"
                }
            ]
        },
        {
            "notificationsubsribe": [
                {
                    "name": "Can add notification subsribe",
                    "codename": "add_notificationsubsribe"
                },
                {
                    "name": "Can change notification subsribe",
                    "codename": "change_notificationsubsribe"
                },
                {
                    "name": "Can delete notification subsribe",
                    "codename": "delete_notificationsubsribe"
                },
                {
                    "name": "Can view notification subsribe",
                    "codename": "view_notificationsubsribe"
                }
            ]
        },
        {
            "usernotificationread": [
                {
                    "name": "Can add user notification read",
                    "codename": "add_usernotificationread"
                },
                {
                    "name": "Can change user notification read",
                    "codename": "change_usernotificationread"
                },
                {
                    "name": "Can delete user notification read",
                    "codename": "delete_usernotificationread"
                },
                {
                    "name": "Can view user notification read",
                    "codename": "view_usernotificationread"
                }
            ]
        },
        {
            "session": [
                {
                    "name": "Can add session",
                    "codename": "add_session"
                },
                {
                    "name": "Can change session",
                    "codename": "change_session"
                },
                {
                    "name": "Can delete session",
                    "codename": "delete_session"
                },
                {
                    "name": "Can view session",
                    "codename": "view_session"
                }
            ]
        },
        {
            "user": [
                {
                    "name": "Can add user",
                    "codename": "add_user"
                },
                {
                    "name": "Can Generate Login Credentials",
                    "codename": "can_generate_login_credentials"
                },
                {
                    "name": "Can change user",
                    "codename": "change_user"
                },
                {
                    "name": "Can delete user",
                    "codename": "delete_user"
                },
                {
                    "name": "Can view user",
                    "codename": "view_user"
                }
            ]
        }
    ]
}
```
