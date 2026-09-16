import subprocess
import time

def run_adb_command(command_list):
    """Helper function to run ADB commands safely."""
    return subprocess.run(command_list, capture_output=True, text=True, check=True)

def main():
    print("🤖 [INFO] Scanning for connected Android devices...")
    time.sleep(1) # For dramatic effect
    
    try:
        # 1. Get Android Version
        version_result = run_adb_command(['adb', 'shell', 'getprop', 'ro.build.version.release'])
        android_version = version_result.stdout.strip()
        
        # 2. Get Device Model
        model_result = run_adb_command(['adb', 'shell', 'getprop', 'ro.product.model'])
        device_model = model_result.stdout.strip()
        
        if android_version and device_model:
            print(f"🎉 [SUCCESS] Device Found: {device_model}")
            print(f"📱 [SUCCESS] Android Version: OS {android_version}")
            print("🚀 [INFO] Sending the ultimate sigma notification...")
            
            # 3. Send Your Custom Ridiculous Notification
            # Note: Single quotes inside double quotes to prevent syntax errors in terminal shell
            notification_title = "⚠️ SYSTEM ALERT"
            notification_body = "if you you read this notification you are 67 sigma and also you spend 20 kb storage on your computer most 67 way posbble"
            
            run_adb_command([
                'adb', 'shell', 'cmd', 'notification', 'post', 
                '-t', notification_title, 
                'sigma_tag', notification_body
            ])
            
            print("😎 [DONE] Check your phone right now. You are officially 67 sigma.")
        else:
            print("❓ [ERROR] Device detected but couldn't retrieve info. Is the screen unlocked?")
            
    except FileNotFoundError:
        print("❌ [ERROR] 'adb' command not found. Please install ADB and add it to your system PATH.")
    except subprocess.CalledProcessError:
        print("❌ [ERROR] No device found! Check your USB cable and make sure 'USB Debugging' is enabled.")

if __name__ == "__main__":
    main()

