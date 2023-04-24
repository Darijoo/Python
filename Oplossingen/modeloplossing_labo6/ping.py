import subprocess
import platform


def run(host_name, aantal_frames):
    """Deze functie neemt een hostname en het aantal frames dat moet gestuurd worden. De functie geeft een list terug met volgende elementen:
    - Het percentage aan packets dat verloren gegaan is
    - Min round-trip tijd in ms
    - Avg round-trip tijd in ms
    - Max round-trip tijd in ms
    - Stddev round-trip tijd in ms"""
    try:
        parameter = "-n" if platform.system().lower() == "windows" else "-c"
        response = subprocess.check_output(
            ["ping", parameter, str(aantal_frames), host_name],
            stderr=subprocess.STDOUT,  # get all output
            universal_newlines=True,  # return string not bytes
        )
    except subprocess.CalledProcessError:
        response = [None]
        return response
    else:
        if platform.system().lower() == "windows":
            packets_lost = response[
                response.find("Lost = ") + 10 : response.find("loss") - 2
            ]
            minimum = response[
                response.find("Minimum = ") + 10 : response.find("ms, Maximum")
            ]
            average = response[response.find("Average = ") + 10 : response.rfind("ms")]
            maximum = response[
                response.find("Maximum = ") + 10 : response.find("ms, Average")
            ]
            stddev = "-"
            mijn_list = []
            mijn_list.append(packets_lost)
            mijn_list.append(minimum)
            mijn_list.append(average)
            mijn_list.append(maximum)
            mijn_list.append(stddev)
            return mijn_list
        else:
            packets_lost = response[
                response.find("packets received")
                + 18 : response.find("packet loss")
                - 2
            ]
            round_trip = response[
                response.find("stddev") + 9 : response.rfind("ms") - 1
            ]
            return_string = packets_lost + "/" + round_trip
            return return_string.split("/")
