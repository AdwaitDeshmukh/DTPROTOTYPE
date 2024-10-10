import matplotlib.pyplot as plt

def plot_bar_with_thresholds(consumption, save_path=None):
    # Handle invalid values
    if consumption is None or consumption < 0:
        print("Invalid consumption value. Please provide a valid number.")
        return
    
    thresholds = {
        100: 'green',
        250: 'yellow',
        400: 'orange',
        500: 'red'
    }

    def get_color(consumption):
        for threshold, color in sorted(thresholds.items(), reverse=True):
            if consumption >= threshold:
                return color
        return 'green'

    color = get_color(consumption)

    # Create the bar plot
    fig, ax = plt.subplots()
    ax.bar(0, consumption, color=color, width=0.5)

    # Set dynamic y-axis limits
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(0, max(consumption + 50, 550))

    # Add horizontal threshold lines and labels
    for threshold in thresholds.keys():
        ax.axhline(y=threshold, color='black', linestyle='--', linewidth=1)
        ax.text(0.1, threshold + 5, f'{threshold}', color='black')

    # Add a label to the bar
    ax.text(0, consumption + 10, f'{consumption}', ha='center', va='bottom', color='black')

    # Set labels and title
    ax.set_xticks([])
    ax.set_ylabel('Consumption')
    ax.set_title(f'Consumption: {consumption}')
    ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

    # Optionally save the plot to a file
    if save_path:
        plt.savefig(save_path)

    plt.show()

if __name__ == "__main__":
    consumption = 300
    plot_bar_with_thresholds(consumption)
