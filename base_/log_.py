#! python2.7#*-* coding=utf-8 -*-import osimport sysimport logging.configimport loggingdef mylog(logFileName=None, stdoutOn=False):     if logFileName is not None:        basename = os.path.basename(logFileName)        dirname = os.path.dirname(logFileName)        logfile = basename.split('.')[0] + '.log'    else:        logfile = 'log.log'    logger = logging.getLogger()    if os.path.exists(logfile):        os.remove(logfile)        if stdoutOn != False:        formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(lineno)s] %(message)s')        handler = logging.StreamHandler(sys.stdout)        handler.setFormatter(formatter)        logger.addHandler(handler)        formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(lineno)s] %(message)s')    handler = logging.FileHandler(logfile, encoding='utf-8')    handler.setFormatter(formatter)    logger.addHandler(handler)    logger.setLevel(logging.DEBUG)    return logger