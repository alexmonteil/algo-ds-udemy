# Write a function that converts AM/PM time to military time from the form HH:MM:SSAM to HH:MM:SS
def timeConversion(s):
    hours = int(s[:2])
    denom = s[-2:]
    
    if (denom == "AM"):
        if hours < 12:
            return s[:8]
        else:
            newhours = hours - 12
            if newhours >= 10:
                return f"{newhours}" + s[2:8]
            else:
                return f"0{newhours}" + s[2:8]
    else:
        if hours < 12:
            return f"{hours + 12}" + s[2:8]
        else:
            return s[:8]
        
        
        
# Testing 

time = "12:01:45AM"

print(timeConversion(time))
    
    