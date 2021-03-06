from job import job
import os

datadirname = 'analysis_data'
plotdirname = 'analysis_plots'
minfile = os.path.join('100K_Structure_minimization', 'finaltraj.lammpstrj')


# Loop for each path
for item in os.walk('../../'):

    path = item[0]

    # Filter for paths that contain jobs
    if 'job' not in path:
        continue
    if datadirname in path:
        continue
    if plotdirname in path:
        continue
    if 'minimization' in path:
        continue

    error = False
    try:
        run = job(path)
    except Exception:
        error = True
        pass

    try:
        run.apd()
    except Exception:
        error = True
        pass

    try:
        run.etg()
    except Exception:
        error = True
        pass

    try:
        run.vtg()
    except Exception:
        error = True
        pass

    try:
        run.apd_single(os.path.join(path, minfile))
    except Exception:
        error = True
        pass

    try:
        run.save_data()
    except Exception:
        error = True
        pass

    if error:
        errorfile = os.path.join(path, 'error.txt')
        with open(errorfile, 'a') as f:
            f.write('error in analysis')

    print('-'*79)
