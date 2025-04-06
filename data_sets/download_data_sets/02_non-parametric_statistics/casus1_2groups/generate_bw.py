import numpy as np
import pandas as pd

def create_right_skewed_bodyweight_data(mean1, mean2, std, replicates=12, filename="bodyweight_data.csv"):
    """
    Creates right-skewed bodyweight data for two diets with specified means and standard deviation, and saves it to a CSV file.

    Args:
        mean1 (float): Mean bodyweight for diet 1.
        mean2 (float): Mean bodyweight for diet 2.
        std (float): Standard deviation of the data.
        replicates (int): Number of replicates per diet.
        filename (str): Name of the CSV file to save the data to.
    """

    # Generate right-skewed data using a log-normal distribution
    def generate_skewed_data(mean, std, replicates):
        # Calculate parameters for log-normal distribution
        mu = np.log(mean**2 / np.sqrt(mean**2 + std**2))
        sigma = np.sqrt(np.log(1 + (std**2 / mean**2)))
        data = np.random.lognormal(mean=mu, sigma=sigma, size=replicates)
        return data

    diet1_data = generate_skewed_data(mean1, std, replicates)
    diet2_data = generate_skewed_data(mean2, std, replicates)

    # Create DataFrame
    df = pd.DataFrame({
        'Diet': ['Diet 1'] * replicates + ['Diet 2'] * replicates,
        'Bodyweight': np.concatenate([diet1_data, diet2_data])
    })

    # Save DataFrame to CSV
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Set parameters
mean1 = 50  # Mean bodyweight for diet 1
mean2 = mean1 + (1.5 * 10) # 1.5 standard deviations higher
std = 10    # Standard deviation
replicates = 48
filename = "bodyweight_data.csv" # filename

# Create and save the dataset
create_right_skewed_bodyweight_data(mean1, mean2, std, replicates, filename)