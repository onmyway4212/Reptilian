import threading
threadobj = threading.Thread(target=print, args = ['cat','dog','freogs'],
                             kwargs = {'sep': ' & '})
threadobj.start()