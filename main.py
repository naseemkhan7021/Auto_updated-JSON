import json,os,time,schedule


def wrietJson(data, json_file='Storege.json'):
    with open(json_file, 'w') as jsonWriting:
        json.dump(data, jsonWriting,indent=4,sort_keys=True)

old_files = []

def job():
    newfils = os.listdir('jsonfiles')

    global old_files

    for File in newfils:
        if File in old_files:
            pass
        else:
            file_details = {}

            fileStatic_info = os.stat('jsonfiles/'+File)
            # slice the usefull data
            ctime, mtime, size = fileStatic_info[-1], fileStatic_info[-2], fileStatic_info[6]
            # print(ctime,mtime,size)

            file_details['Date Created'] = time.ctime(ctime)  # create date
            file_details['Date Modified'] = time.ctime(mtime)  # modified date
            file_details['File Name'] = File
            file_details['File Extension'] = '.'+File.split('.')[-1]
            file_details['File Size (byts)'] = size

            old_files.append(File)
            try:
                with open('Storege.json') as jsondata:
                    data = json.load(jsondata)
                    # locate where to store the data in json 
                    temp = data['filesDetails']
                    # appanditn the data in the dict 
                    temp.append(file_details)
                # write the data in the json
                wrietJson(data)
                file_details = {}
                print(f'The {File} details is added succefully')

            except ValueError:  # includes simplejson.decoder.JSONDecodeError
                print ('Json decode error')






job()
# now to sate the schule of doing the job
schedule.every().minutes.do(job)


while True:
    print('Scanning.....')
    schedule.run_pending()
    time.sleep(60)



# print(os.listdir('Storege.json'))