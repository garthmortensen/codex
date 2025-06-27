# Cron Syntax

```
* * * * *  command_to_execute
```

# Special Characters

- `*`: Matches any value.
- `,`: Separates multiple values (e.g., `1,15`).
- `-`: Specifies a range of values (e.g., `1-5`).
- `/`: Specifies increments (e.g., `*/15`).

# Common Examples

- **Run a script every minute:**

  ```
  * * * * * /path/to/script.sh
  ```

- **Run a script every hour:**

  ```
  0 * * * * /path/to/script.sh
  ```

- **Run a script at midnight:**

  ```
  0 0 * * * /path/to/script.sh
  ```

# Crontab Management

- `crontab -e`: Edit the current user's crontab file.
- `crontab -l`: List the current user's cron jobs.
- `crontab -r`: Remove the current user's crontab.
- `sudo crontab -u user -e`: Edit another user's crontab.
- `sudo service crond restart`: Restart the cron daemon.

# Permissions & Environment

- **Permissions**: The script or command must be executable (`chmod +x /path/to/script.sh`).
- **Environment**: Cron jobs run in a limited environment. Specify full paths and necessary environment variables.

# Logging Cron Jobs

To log the output of a cron job, you can redirect its standard output and standard error streams to a file.

- **Append output to a log file:**

  ```
  * * * * * /path/to/script.sh >> /path/to/logfile.log 2>&1
  ```

# Useful Resources

- [Crontab Guru](https://crontab.guru/): An online editor and tester for cron schedules.

# cron.md

## Cron Basics

```bash
crontab -e                   # Edit current user's crontab
crontab -l                   # List current user's cron jobs
crontab -r                   # Remove current user's crontab
sudo crontab -u user -e      # Edit another user's crontab
sudo service crond restart   # Restart cron daemon
```

## Cron Format

```
* * * * * command            # Min Hour Day Month DayOfWeek
┌───────────── minute (0-59)
│ ┌─────────── hour (0-23)
│ │ ┌───────── day of month (1-31)
│ │ │ ┌─────── month (1-12)
│ │ │ │ ┌───── day of week (0-6, Sunday=0)
│ │ │ │ │
* * * * *
```

## Common Patterns

```bash
0 0 * * *                   # Daily at midnight
0 */6 * * *                 # Every 6 hours
30 2 * * 1                  # Every Monday at 2:30 AM
0 9-17 * * 1-5              # Every hour 9-5, weekdays only
*/15 * * * *                # Every 15 minutes
0 0 1 * *                   # First day of every month
0 0 * * 0                   # Every Sunday at midnight
```

## Special Strings

```bash
@reboot                     # Run once at startup
@yearly                     # Run once a year (0 0 1 1 *)
@annually                   # Same as @yearly
@monthly                    # Run once a month (0 0 1 * *)
@weekly                     # Run once a week (0 0 * * 0)
@daily                      # Run once a day (0 0 * * *)
@midnight                   # Same as @daily
@hourly                     # Run once an hour (0 * * * *)
```

## Data Science Examples

```bash
# Daily ETL pipeline at 2 AM
0 2 * * * /path/to/venv/bin/python /opt/etl/daily_pipeline.py

# Model training every Sunday at 3 AM
0 3 * * 0 /path/to/venv/bin/python /opt/ml/train_model.py

# Data backup every 6 hours
0 */6 * * * /opt/scripts/backup_data.sh

# Log rotation monthly
0 0 1 * * /usr/sbin/logrotate /etc/logrotate.conf
```

## Cron Best Practices

- Always use absolute paths for commands and files
- Set environment variables at the top of crontab
- Redirect output: > /dev/null 2>&1 or >> /var/log/cron.log
- Test scripts manually before adding to cron
- Use /var/log/cron for debugging cron issues