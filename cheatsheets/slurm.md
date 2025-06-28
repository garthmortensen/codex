# slurm.md

## Job Submission

```bash
sbatch script.sh             # Submit batch job
sbatch --job-name=myjob script.sh  # Submit with job name
sbatch --partition=gpu script.sh   # Submit to specific partition
sbatch --time=01:30:00 script.sh   # Set time limit (1h 30m)
sbatch --nodes=2 script.sh    # Request 2 nodes
sbatch --ntasks=8 script.sh   # Request 8 tasks
sbatch --cpus-per-task=4 script.sh # Request 4 CPUs per task
sbatch --mem=16G script.sh    # Request 16GB memory
sbatch --gres=gpu:2 script.sh # Request 2 GPUs
srun command                  # Run interactive job
srun --pty bash              # Interactive shell
```

## Job Monitoring

```bash
squeue                       # Show all jobs in queue
squeue -u username           # Show jobs for specific user
squeue -j jobid              # Show specific job
squeue -p partition          # Show jobs in partition
squeue --format="%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R"  # Custom format
sinfo                        # Show partition/node info
sinfo -N                     # Show node-oriented info
sinfo -p partition           # Show specific partition
sacct                        # Show completed jobs
sacct -j jobid               # Show specific job accounting
sacct --format=JobID,JobName,Partition,Account,AllocCPUS,State,ExitCode  # Custom accounting format
```

## Job Control

```bash
scancel jobid                # Cancel specific job
scancel -u username          # Cancel all user jobs
scancel --name=jobname       # Cancel jobs by name
scancel --partition=gpu      # Cancel jobs in partition
scontrol hold jobid          # Hold job
scontrol release jobid       # Release held job
scontrol show job jobid      # Show detailed job info
scontrol show node nodename  # Show node details
scontrol show partition      # Show partition info
```

## Resource Information

```bash
sinfo -o "%20N %10c %10m %25f %10G"  # Nodes with CPU, memory, features, GRES
sinfo --format="%20N %.6D %9P %.11T %.4c %.8z %.6m %.8d %.6w %.8f %20E"  # Detailed node info
squeue --format="%.8i %.8u %.12a %.10P %.20j %.3t %.6D %.6C %.10M %.10l"  # Detailed queue
sacct -S 2025-06-01          # Accounting since date
sacct --starttime=2025-06-01 --endtime=2025-06-26  # Date range
sprio -j jobid               # Show job priority
sprio -u username            # Show user job priorities
```

## Job Script Examples

```bash
#!/bin/bash
#SBATCH --job-name=ml-training
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --gres=gpu:1
#SBATCH --time=02:00:00
#SBATCH --output=job_%j.out
#SBATCH --error=job_%j.err

# Load modules
module load python/3.11
module load cuda/11.8

# Activate environment
source venv/bin/activate

# Run training
python train_model.py --epochs=100 --batch-size=64
```

## Array Jobs

```bash
#!/bin/bash
#SBATCH --job-name=param-sweep
#SBATCH --array=1-10
#SBATCH --partition=compute
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=01:00:00

# Use array task ID as parameter
python experiment.py --param=${SLURM_ARRAY_TASK_ID}
```

## Data Science Workflow

```bash
# 1. Submit preprocessing job
sbatch --job-name=preprocess --mem=16G preprocess.sh

# 2. Submit dependent training job
sbatch --dependency=afterok:jobid --job-name=train --gres=gpu:1 train.sh

# 3. Monitor progress
watch -n 5 squeue -u $USER

# 4. Check resource usage
sacct -j jobid --format=JobID,MaxRSS,MaxVMSize,AveCPU,ElapsedTime
```