def update_server_config (config_file, key, value):
    with open(config_file, "r") as file:
        lines = file.readlines()

    with open (config_file, "w") as file:
        for line in lines:
            if key in line:
             file.write(key + "=" + value + "\n")
            else:
             file.write(line)

config_file = "server.conf"
key = "MAX_CONNECTIONS"
value = "1800"
update_server_config(config_file, key, value)
