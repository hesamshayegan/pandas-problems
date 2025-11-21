# stratascratch - medium

import pandas as pd

# create a day-only column from timestamp
df = facebook_web_log.copy()
df['day'] = df['timestamp'].dt.floor('d')

# filter page_load and page_exit events
page_loads = df[df['action'] == 'page_load']
page_exits = df[df['action'] == 'page_exit']

# get latest page_load per user per day
latest_loads = (
    page_loads
    .groupby(['user_id', 'day'])
    .agg(load_time=('timestamp', 'max'))
    .reset_index()
)

# get earliest page_exit per user per day
earliest_exits = (
    page_exits
    .groupby(['user_id', 'day'])
    .agg(exit_time=('timestamp', 'min'))
    .reset_index()
)

# merge load and exit events
sessions = pd.merge(
    latest_loads,
    earliest_exits,
    on=['user_id', 'day']
)

# keep only valid sessions where load is before exit
sessions = sessions[sessions['load_time'] < sessions['exit_time']]

# calculate session duration in seconds
sessions['session_duration'] = (sessions['exit_time'] - sessions['load_time']).dt.total_seconds()

# compute average session duration per user
result = (
    sessions.groupby('user_id')['session_duration']
    .mean()
    .reset_index()
    .rename(columns={'session_duration': 'avg_session_duration'})
)

result


# first question I should ask: average session time on what? (across days?)

# the reason I need a "day" column:
# if I don't use an additional day column when I wanna aggregate on timestamp:
# df.groupby(['user_id', 'timestamp']).agg({'timestamp': 'max'})
# pandas will treat each timestamp as a separate group.
# so I need a common part of timestap (day) that helps me to group the events on a daily basis


# when I group by ["user_id", "date"], pandas automatically sets those columns aside as the index (or as grouping keys).