from sklearn.cluster import KMeans
import pandas as pd

from plot_generator import PlotGenerator


class ClusteringModel:
    numerical_values = ['Life Ladder', 'Log GDP per capita', 'Social support',
                        'Healthy life expectancy at birth',
                        'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Positive affect',
                        'Negative affect',
                        'Confidence in national government', 'Democratic Quality', 'Delivery Quality',
                        'Standard deviation of ladder by country-year', 'Standard deviation of ladder by country-year']

    def __init__(self, data_path):
        '''
        Load Data from excel to DataFrame
        :param data_path: path to excel file
        '''
        self.data_frame = pd.read_excel(data_path)

    def preprocess(self):
        '''
        Preprocess data from the excel
        Remove 'Year' column because its not informative
        Complete missing values of numerical columns by Standardization
        Set 'Contry' column as index
        :return: DataFrame after the preprocess ready for clustering
        '''
        self.data_frame.drop('year', axis=1, inplace=True)
        for column in self.numerical_values:
            column_avg = self.data_frame[column].mean()
            column_std = self.data_frame[column].std()
            # fill NA values
            self.data_frame[column].fillna(self.data_frame[column].mean(), inplace=True)
            # normalize column by - Standardization
            normalization_func = lambda x: (x - column_avg) / column_std
            self.data_frame[column] = self.data_frame[column].apply(normalization_func)
            # Aggregate values by country, average rest of the fields.
            self.data_frame = self.data_frame.groupby(['country'], as_index=False).mean()
        self.countries = self.data_frame[['country']].copy()
        self.data_frame = self.data_frame.set_index('country')
        print self.data_frame


    def k_means(self, n_clusters, num_of_runs):
        '''
        run k-means and save the results at self.countries
        :param n_clusters: number of clusters
        :param num_of_runs: number of runs
        :return: DataFrame containing all data for output : ( 'Country','Social support', 'Generosity')
        '''
        kmeans = KMeans(n_clusters=n_clusters, random_state=num_of_runs)
        kmeans.fit(self.data_frame)
        kmeans_results = kmeans.predict(self.data_frame)
        self.countries['Social support'] = self.data_frame['Social support'].values
        self.countries['Generosity'] = self.data_frame['Generosity'].values
        self.countries['Cluster'] = kmeans_results
        return self.countries
