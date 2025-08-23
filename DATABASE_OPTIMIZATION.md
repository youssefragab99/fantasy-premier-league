# Database Optimization for Faster Docker Startup

This guide explains how to optimize your Fantasy Premier League database loading to make Docker containers start much faster by pre-loading data.

## Why Optimize Database Loading?

Currently, every time you start your Docker container, it:
1. Waits for PostgreSQL to be ready
2. Runs database migrations
3. Downloads and loads teams data from FPL API
4. Downloads and loads players data from FPL API
5. Loads historical gameweek data

This process can take several minutes, especially when downloading large amounts of data from external APIs.

## Optimization Strategies

### Option 1: Database Dumps (Recommended)

Create a complete database snapshot that can be restored instantly.

#### How It Works

1. **Create a dump** of your fully loaded database
2. **Mount the dump** to PostgreSQL's initialization directory
3. **PostgreSQL automatically restores** the data on first startup
4. **Subsequent starts** use the persistent volume data

#### Benefits

- ⚡ **Instant startup** - no API calls or data processing
- 🔒 **Consistent data** - exact same data every time
- 📦 **Portable** - can share dumps between team members
- 🚀 **Production ready** - reliable and fast

#### Setup Steps

1. **Create the database dump directory:**
   ```bash
   mkdir -p database_dumps
   ```

2. **Add the volume mount to docker-compose.yml (already done):**
   ```yaml
   volumes:
     - ./database_dumps:/docker-entrypoint-initdb.d
   ```

3. **Create your first dump:**
   ```bash
   # Start your containers and let them load data normally
   docker-compose up
   
   # In another terminal, create a dump once data is loaded
   python scripts/create_dump.py
   ```

4. **Use fast mode for subsequent starts:**
   ```bash
   # Stop containers
   docker-compose down
   
   # Remove the persistent volume to force fresh start
   docker-compose down -v
   
   # Start with fast mode (will use the dump)
   FAST_MODE=true docker-compose up
   ```

#### Scripts Available

- **`scripts/create_dump.py`** - Creates a PostgreSQL dump of your database
- **`scripts/restore_dump.py`** - Manually restores a database from a dump file

### Option 2: Persistent Volumes (Simpler)

Keep the database data between container restarts.

#### How It Works

1. **PostgreSQL data persists** in the `pgdata` volume
2. **No data reloading** on subsequent starts
3. **Data survives** container restarts and rebuilds

#### Benefits

- 🚀 **Fast startup** - no data loading needed
- 💾 **Persistent** - data survives container lifecycle
- 🔧 **Simple** - no additional setup required

#### Setup

This is already configured in your `docker-compose.yml`:
```yaml
volumes:
  - pgdata:/var/lib/postgresql/data
```

#### Usage

```bash
# First time - loads data normally
docker-compose up

# Subsequent starts - uses existing data
docker-compose down
docker-compose up  # Fast startup!
```

### Option 3: Hybrid Approach (Best of Both)

Combine both strategies for maximum flexibility.

#### How It Works

1. **Use persistent volumes** for development
2. **Create dumps** for production deployments
3. **Choose strategy** based on your needs

#### Environment Variables

```bash
# Skip data loading (use existing data)
SKIP_DATA_LOADING=true docker-compose up

# Fast mode (use dump if available, skip API calls)
FAST_MODE=true docker-compose up

# Normal mode (load data from APIs)
docker-compose up
```

## Performance Comparison

| Method | Startup Time | Data Freshness | Complexity |
|--------|--------------|----------------|------------|
| **Fresh API Load** | 3-5 minutes | Always fresh | Low |
| **Persistent Volume** | 10-30 seconds | Stale until refresh | Low |
| **Database Dump** | 10-30 seconds | Stale until refresh | Medium |
| **Hybrid** | 10-30 seconds | Configurable | Medium |

## Best Practices

### For Development

```bash
# Use persistent volumes for daily development
docker-compose up
# ... work with data ...
docker-compose down
docker-compose up  # Fast restart!
```

### For Production

```bash
# Create a dump after data updates
python scripts/create_dump.py

# Deploy with fast mode
FAST_MODE=true docker-compose up
```

### For Team Collaboration

```bash
# Share the database dump with your team
git add database_dumps/fpl_dump_*.sql
git commit -m "Add database dump for fast startup"
git push

# Team members can now start instantly
git pull
FAST_MODE=true docker-compose up
```

## Troubleshooting

### Dump Creation Fails

```bash
# Check if PostgreSQL is running
docker-compose ps

# Verify connection details
echo $DATABASE_URL

# Try manual connection
psql $DATABASE_URL -c "SELECT version();"
```

### Dump Restoration Fails

```bash
# Check dump file exists
ls -la database_dumps/

# Verify file permissions
chmod 644 database_dumps/*.sql

# Check PostgreSQL logs
docker-compose logs db
```

### Performance Issues

```bash
# Check dump file size
du -h database_dumps/*.sql

# Monitor startup time
time docker-compose up

# Use fast mode
FAST_MODE=true docker-compose up
```

## Advanced Configuration

### Custom Dump Options

Edit `scripts/create_dump.py` to customize:
- Compression options
- Schema-only dumps
- Selective table dumps
- Custom file naming

### Automated Dumps

Add to your CI/CD pipeline:
```yaml
# GitHub Actions example
- name: Create database dump
  run: python scripts/create_dump.py
  env:
    DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

### Multiple Environment Dumps

```bash
# Development dump
ENVIRONMENT=dev python scripts/create_dump.py

# Production dump
ENVIRONMENT=prod python scripts/create_dump.py
```

## Conclusion

By implementing these optimization strategies, you can reduce your Docker container startup time from **3-5 minutes to 10-30 seconds**. 

**Recommended approach:**
1. Start with **persistent volumes** (already configured)
2. Add **database dumps** for production deployments
3. Use **hybrid mode** for maximum flexibility

This gives you the best balance of speed, reliability, and maintainability for your Fantasy Premier League data pipeline. 