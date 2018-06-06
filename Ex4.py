from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt


class MyClass:
    numerical_values = ['Life Ladder', 'Log GDP per capita', 'Social support',
                        'Healthy life expectancy at birth',
                        'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Positive affect',
                        'Negative affect',
                        'Confidence in national government', 'Democratic Quality', 'Delivery Quality',
                        'Standard deviation of ladder by country-year', 'Standard deviation of ladder by country-year']

    def __init__(self, data_path, n_clusters, n_init):
        self.n_clusters = n_clusters
        self.n_init = n_init
        self.data_frame = pd.read_excel(data_path)

    def preprocess(self):
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


    def k_means(self):
        kmeans = KMeans(n_clusters=self.n_clusters, random_state=self.n_init)
        kmeans.fit(self.data_frame)
        kmeans_results = kmeans.predict(self.data_frame)
        self.countries['Social support'] = self.data_frame['Social support'].values
        self.countries['Generosity'] = self.data_frame['Generosity'].values
        self.countries['Cluster'] = kmeans_results
        return self.countries




my = MyClass('data.xlsx', 5, 5)
my.preprocess()
my.k_means()
