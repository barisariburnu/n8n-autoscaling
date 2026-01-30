#!/usr/bin/env python3
"""
Redis Queue Monitor

This service monitors the n8n BullMQ queue length in Redis and logs the status
continuously. It helps track queue activity and workflow execution patterns.

Features:
    - Real-time queue length monitoring
    - Support for multiple BullMQ patterns (v3, v4+, legacy)
    - Configurable polling interval
    - Comprehensive error handling

Author: barisariburnu
License: MIT
Repository: https://github.com/barisariburnu/n8n-autoscaling
"""

import redis
import time
import os

# Configuration from environment variables with defaults
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
QUEUE_NAME_PREFIX = os.getenv('QUEUE_NAME_PREFIX', 'bull')  # BullMQ default prefix
QUEUE_NAME = os.getenv('QUEUE_NAME', 'jobs')
POLL_INTERVAL_SECONDS = int(os.getenv('POLL_INTERVAL_SECONDS', 5))


def get_redis_connection():
    """Establishes a connection to Redis.
    
    Returns:
        redis.Redis: Redis connection object if successful, None otherwise
    """
    try:
        r = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            decode_responses=True
        )
        r.ping()
        print(f"Successfully connected to Redis at {REDIS_HOST}:{REDIS_PORT}")
        return r
    except redis.exceptions.ConnectionError as e:
        print(f"Error connecting to Redis: {e}")
        return None


def get_queue_length(r_conn, queue_name_prefix, queue_name):
    """Gets the length of the specified BullMQ queue.
    
    BullMQ stores lists for different states of a queue:
    - 'wait' or 'waiting': pending jobs
    - 'active': currently processing jobs
    - 'delayed': scheduled for future execution
    - 'completed': finished jobs
    - 'failed': jobs that encountered errors
    
    This function checks for the waiting queue using multiple patterns:
    - BullMQ v3+: <prefix>:<queue>:wait
    - BullMQ v4+: <prefix>:<queue>:waiting
    - Legacy: <prefix>:<queue>
    
    Args:
        r_conn: Redis connection object
        queue_name_prefix: Queue prefix (e.g., 'bull')
        queue_name: Queue name (e.g., 'jobs')
        
    Returns:
        int: Queue length, or 0 if queue doesn't exist or on error
    """
    key_to_check = f"{queue_name_prefix}:{queue_name}:wait"
    
    try:
        length = r_conn.llen(key_to_check)
        if length is not None:
            return length
            
        # Try the older pattern if :wait doesn't exist
        key_to_check_legacy = f"{queue_name_prefix}:{queue_name}"
        length = r_conn.llen(key_to_check_legacy)
        if length is not None:
            print(f"Note: Using legacy key pattern '{key_to_check_legacy}' for queue length.")
            return length
            
        # Try BullMQ v4+ pattern
        key_to_check_v4 = f"{queue_name_prefix}:{queue_name}:waiting"
        length = r_conn.llen(key_to_check_v4)
        if length is not None:
            print(f"Note: Using BullMQ v4+ key pattern '{key_to_check_v4}' for queue length.")
            return length
            
        print(
            f"Warning: Key '{key_to_check}', '{key_to_check_legacy}', or "
            f"'{key_to_check_v4}' not found or not a list. Assuming length 0."
        )
        return 0
        
    except redis.exceptions.ResponseError as e:
        # This can happen if the key exists but is not a list type
        print(f"Redis error when checking length of '{key_to_check}': {e}. Assuming length 0.")
        return 0
    except Exception as e:
        print(f"Unexpected error when checking length of '{key_to_check}': {e}. Assuming length 0.")
        return 0


if __name__ == "__main__":
    redis_conn = get_redis_connection()
    
    if redis_conn:
        print(f"Monitoring Redis queue '{QUEUE_NAME_PREFIX}:{QUEUE_NAME}' every {POLL_INTERVAL_SECONDS} seconds...")
        print("Press Ctrl+C to stop.")
        
        try:
            while True:
                length = get_queue_length(redis_conn, QUEUE_NAME_PREFIX, QUEUE_NAME)
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{timestamp}] Queue '{QUEUE_NAME_PREFIX}:{QUEUE_NAME}:wait' length: {length}")
                time.sleep(POLL_INTERVAL_SECONDS)
                
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            
        finally:
            redis_conn.close()
            print("Redis connection closed.")