import speedtest
import psutil
import GPUtil
import tkinter as tk
from tkinter import ttk
import threading

def check_internet_speed():
    st = speedtest.Speedtest()
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    return upload_speed

def check_hardware():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
    
    gpus = GPUtil.getGPUs()
    gpu = gpus[0].name if gpus else "No GPU detected"
    
    return {
        "cpu_usage": cpu,
        "ram": ram,
        "gpu": gpu
    }

def get_streaming_requirements():
    return {
        "youtube": {
            "min_bitrate": 1500,
            "max_bitrate": 12000,
            "recommended_bitrate": 4500,
            "audio_bitrate": 128
        },
        "facebook": {
            "min_bitrate": 1500,
            "max_bitrate": 4000,
            "recommended_bitrate": 3000,
            "audio_bitrate": 128
        }
    }

def calculate_best_settings(upload_speed, hardware, requirements):
    available_bitrate = upload_speed * 1000 * 0.8  # 80% of upload speed in kbps
    recommended_bitrate = min(
        available_bitrate,
        requirements["youtube"]["recommended_bitrate"],
        requirements["facebook"]["recommended_bitrate"]
    )
    
    resolution = "720p"
    fps = 30
    audio_bitrate = 128  # kbps
    audio_sample_rate = 44100  # Hz
    
    if recommended_bitrate >= 4500 and hardware["ram"] >= 16:
        resolution = "1080p"
    
    if recommended_bitrate >= 6000 and "NVIDIA" in hardware["gpu"]:
        fps = 60
    
    if recommended_bitrate >= 6000:
        audio_bitrate = 192
    
    if recommended_bitrate >= 8000:
        audio_sample_rate = 48000
    
    return {
        "resolution": resolution,
        "fps": fps,
        "video_bitrate": int(recommended_bitrate),
        "audio_bitrate": audio_bitrate,
        "audio_sample_rate": audio_sample_rate
    }

def check_settings_thread():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Checking settings...\n")
    
    upload_speed = check_internet_speed()
    hardware = check_hardware()
    requirements = get_streaming_requirements()
    best_settings = calculate_best_settings(upload_speed, hardware, requirements)
    
    root.after(0, update_results, upload_speed, hardware, requirements, best_settings)

def update_results(upload_speed, hardware, requirements, best_settings):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Upload Speed: {upload_speed:.2f} Mbps\n\n")
    
    result_text.insert(tk.END, f"Hardware:\n")
    result_text.insert(tk.END, f"CPU Usage: {hardware['cpu_usage']}%\n")
    result_text.insert(tk.END, f"RAM: {hardware['ram']:.2f} GB\n")
    result_text.insert(tk.END, f"GPU: {hardware['gpu']}\n\n")
    
    result_text.insert(tk.END, "Streaming Requirements:\n")
    result_text.insert(tk.END, f"YouTube: {requirements['youtube']['min_bitrate']}-{requirements['youtube']['max_bitrate']} kbps (video)\n")
    result_text.insert(tk.END, f"Facebook: {requirements['facebook']['min_bitrate']}-{requirements['facebook']['max_bitrate']} kbps (video)\n\n")
    
    result_text.insert(tk.END, "Best Settings:\n")
    result_text.insert(tk.END, f"Resolution: {best_settings['resolution']}\n")
    result_text.insert(tk.END, f"FPS: {best_settings['fps']}\n")
    result_text.insert(tk.END, f"Video Bitrate: {best_settings['video_bitrate']} kbps\n")
    result_text.insert(tk.END, f"Audio Bitrate: {best_settings['audio_bitrate']} kbps\n")
    result_text.insert(tk.END, f"Audio Sample Rate: {best_settings['audio_sample_rate']} Hz\n")

    check_button.config(state=tk.NORMAL)

def start_check():
    check_button.config(state=tk.DISABLED)
    threading.Thread(target=check_settings_thread, daemon=True).start()

# Create GUI
root = tk.Tk()
root.title("Livestream Settings Calculator")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

check_button = ttk.Button(frame, text="Check Settings", command=start_check)
check_button.grid(row=0, column=0, sticky=tk.W, pady=5)

result_text = tk.Text(frame, width=50, height=20)
result_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.mainloop()