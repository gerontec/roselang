# Office/Business / Scheduling

[Index](README.md) · 8 packages in this topic, 2 more listed under another topic, by downloads.

### ortools

Google OR-Tools python libraries and modules

`pip install ortools` · installs (wheel) · licence: Apache Software License · rank 1472 · last release 2026-01-14 · [PyPI](https://pypi.org/project/ortools/)

<details><summary>README extract</summary>

This project hosts operations research tools developed at Google and
made available as open source under the Apache 2.0 License.

OR-Tools includes solvers for:

- Constraint Programming
 - CP-SAT solver: A constraint programming solver that uses SAT (satisfiability)
 methods.
 - Original CP solver: A constraint programming solver. ...

</details>

### recurring-ical-events

Calculate recurrence times of events, todos, alarms and journals based on icalendar RFC5545.

`pip install recurring-ical-events` · installs (wheel) · licence: LGPL-3.0-or-later · rank 2231 · last release 2026-04-30 · [PyPI](https://pypi.org/project/recurring-ical-events/) · [docs](https://github.com/niccokunzmann/python-recurring-ical-events) · [source](https://github.com/niccokunzmann/python-recurring-ical-events)

_README extract left out: share-alike licence._

### caldav

CalDAV (RFC4791) client library

`pip install caldav` · installs (wheel) · licence: GPL-3.0-or-later OR Apache-2.0 · rank 4946 · last release 2026-10-29 · [PyPI](https://pypi.org/project/caldav/) · [docs](https://caldav.readthedocs.io/) · [source](https://github.com/python-caldav/caldav)

_README extract left out: share-alike licence._

### ics

Python icalendar (rfc5545) parser

`pip install ics` · installs (wheel) · licence: Apache Software License · rank 6651 · last release 2026-04-15 · [PyPI](https://pypi.org/project/ics/)

<details><summary>README extract</summary>

Original repository (GitHub) -
Bugtracker and issues (GitHub) -
PyPi package (ics) -
Documentation (Read The Docs).

Ics.py is a pythonic and easy iCalendar library.
Its goals are to read and write ics data in a developer friendly way.

iCalendar is a widely-used and useful format but not user friendly. ...

Example:
```python
from ics import Calendar, Event
c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '2014-01-01 00:00:00'
c.events.add(e)
c.events
# [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
with open('my.ics', 'w') as my_file:
    my_file.writelines(c.serialize_iter())
# and it's done !
```

Sections: Ics.py : iCalendar for Humans, Quickstart, Documentation, Links

</details>

### businesstimedelta

Timedelta for business time. Supports exact amounts of time (hours, seconds), custom schedules, holidays, and time zones.

`pip install businesstimedelta` · installs (wheel) · licence: MIT License · rank 7128 · last release 2019-09-07 · [PyPI](https://pypi.org/project/businesstimedelta/)

<details><summary>README extract</summary>

Python's timedelta for business time. This module helps you calculate the exact working time between two datetimes. It supports common scenarios such as custom schedules, holidays, and time zones.

Example:
```python
import datetime
import pytz
import businesstimedelta

# Define a working day
workday = businesstimedelta.WorkDayRule(
    start_time=datetime.time(9),
    end_time=datetime.time(18),
    working_days=[0, 1, 2, 3, 4])

# Take out the lunch break
lunchbreak = businesstimedelta.LunchTimeRule(
    start_time=datetime.time(12),
...
```

Sections: BusinessTimeDelta, Example Use, Timezones, Overnight Shifts

</details>

### npmai-agents

Production-grade autonomous AI agent framework with 1,371 tools across 100 classes and a 5-role LLM pipeline — built on the NPMAI ECOSYSTEM.

`pip install npmai-agents` · installs (wheel) · licence: MIT License · rank 7790 · last release 2026-07-07 · [PyPI](https://pypi.org/project/npmai-agents/) · [docs](https://npmai.netlify.app) · [source](https://github.com/sonuramashishnpm/npmai-agent)

<details><summary>README extract</summary>

`🌐 Website` · `📦 PyPI` · `🐙 GitHub` · `👤 Founder`
. ****

npmai_agents is a production-grade, open-source autonomous AI agent framework with 1,371 verified tools across 100 classes — the largest open-source local tool registry ever built. ...

Example:
```python
# Agent brain only
from npmai_agents import AgentBrain

# Specific tools, no matter which internal file they live in
from npmai_agents import StripeTool, GitHubTool, FFmpegTool

# LLM backends
from npmai_agents import GroqBackend, OpenAIBackend, AnthropicBackend

# Core infra
from npmai_agents import CredStore, Workspace, LLMBackend

...
```

...

</details>

### ical

Python iCalendar implementation (rfc 5545) with built-in recurring event support

`pip install ical` · installs (wheel) · licence: Apache-2.0 · rank 8967 · last release 2026-10-20 · [PyPI](https://pypi.org/project/ical/) · [docs](https://allenporter.github.io/ical/) · [source](https://github.com/allenporter/ical)

<details><summary>README extract</summary>

A modern Python RFC 5545 iCalendar library with built-in recurring event support — no companion libraries needed.

Features:
Most Python iCalendar libraries require two separate packages to handle recurring events:

`ical` handles this natively with a single, unified `Timeline` interface, with a Pythonic API and validated inputs. ...

Example:
```python
from ical.calendar_stream import IcsCalendarStream

cal = IcsCalendarStream.calendar_from_ics(ics_content)

# Recurring events are automatically expanded — just iterate
for event in cal.timeline:
    print(event.start, event.summary)
```

...

</details>

### calendaring-config

The shared configuration file of caldav, calendaring and calendaring-jmap: format, discovery and credentials

`pip install calendaring-config` · installs (wheel) · licence: GPL-3.0-or-later OR Apache-2.0 · rank 12011 · last release 2026-10-22 · [PyPI](https://pypi.org/project/calendaring-config/) · [source](https://github.com/pycalendar/calendaring-config)

_README extract left out: share-alike licence._

## Also in this topic

- [holidays](file-formats-json.md#holidays) - Open World Holidays Framework
- [fiscalyear](office-business-financial.md#fiscalyear) - Utilities for managing the fiscal calendar
