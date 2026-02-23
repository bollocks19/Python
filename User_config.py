test_settings ={
    "Car":"Mazda",
    "Job":"Engineer",
    "Personality":"Kind"
}

        
def add_setting(settings, new_pair):
    key = new_pair[0].lower()
    value = new_pair[1].lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else: settings.update({key:value}) 
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings1, new_pair2):
    key = new_pair2[0].lower()
    value = new_pair2[1].lower()
    if key in settings1:
        settings1.update({key:value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else: 
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key1=key.lower()
    if key1 in settings:
        del settings[key1]
        return f"Setting '{key}' deleted successfully!"
    else: return"Setting not found!"
def view_settings(settings):
    if settings=={}:
        return "No settings available."
    else: 
        lines=["Current User Settings:"]
        for key, value in settings.items():
           lines.append(f"{key.capitalize()}: {value}")
    
        return "\n".join(lines) + "\n"
        

        

