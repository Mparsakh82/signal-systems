import numpy as np
import matplotlib.pyplot as plt

# Function to check if the signal is periodic
def is_periodic(signal):
    N = len(signal)
    
    # Check possible periods from 1 to N-1
    for T in range(1, N):
        periodic = True
        for i in range(N - T):
            if signal[i] != signal[i + T]:
                periodic = False
                break
        if periodic:
            return True, T  # The signal is periodic with period T
    return False, None  # The signal is not periodic

# Function to plot the signal and show periodicity result
def plot_signal(signal):
    n = np.arange(len(signal))  # Time axis
    is_periodic_signal, period = is_periodic(signal)
    
    # Plot the signal using plt.bar instead of plt.stem
    plt.bar(n, signal, width=0.3, color='b', align='center')
    plt.title('Discrete Signal')
    plt.xlabel('n (samples)')
    plt.ylabel('x[n]')
    plt.grid(True)
    
    # Display the periodicity result
    if is_periodic_signal:
        plt.text(len(signal) // 2, max(signal) * 0.9, f'The signal is periodic with period {period}', color='green', fontsize=12, bbox=dict(facecolor='white', alpha=0.6))
    else:
        plt.text(len(signal) // 2, max(signal) * 0.9, 'The signal is not periodic', color='red', fontsize=12, bbox=dict(facecolor='white', alpha=0.6))
    
    # Show the plot
    plt.show()

# Example of a discrete signal
signal = [1, 2, 1, 2, 1, 2]  # A periodic signal with period 2

# Plot the signal and display the result
plot_signal(signal)