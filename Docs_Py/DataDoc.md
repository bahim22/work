# Info of methods and functions used

## Data practice

1. Setup root dir & *virtual_env* then sourced data in csv form.
2. Activated env and ran pip install packages needed for notebook
3. Created Jupyter notebook and imported packages
4. Created variable to read the variables in DataFrame
5. Review and clean the data to remove errors
   1. e.g. missing values written as ? need to be replaced as NaN so pandas can create expected data type of numeric instead of object for age column
6. Plot the data

## `method` data.replace(arg1,arg2)

1. Replace values given in *to_replace* with *value*. Values of the DataFrame are replaced with other values dynamically.

```py
>>> df.replace(regex=[r'^ba.$', 'foo'], value='new')
        A    B
0   new  abc
1   new  new
2  bait  xyz
Compare the behavior of s.replace({'a': None}) and s.replace('a', None) to understand the peculiarities of the to_replace parameter:

>>> s = pd.Series([10, 'a', 'a', 'b', 'a'])
When one uses a dict as the to_replace value, it is like the value(s) in the dict are equal to the value parameter.
s.replace({'a': None}) is equivalent to s.replace(to_replace={'a': None}, value=None, method=None):

>>> s.replace({'a': None})
0      10
1    None
2    None
3       b
4    None
dtype: object
When value is not explicitly passed and to_replace is a scalar, list or tuple, replace uses the method parameter (default 'pad') to do the replacement. So this is why the 'a' values are being replaced by 10 in rows 1 and 2 and 'b' in row 4 in this case.

>>> s.replace('a')
0    10
1    10
2    10
3     b
4     b
dtype: object
On the other hand, if None is explicitly passed for value, it will be respected:

>>> s.replace('a', None)
0      10
1    None
2    None
3       b
4    None
dtype: object
1. parameters (to_replace: )
   1. value : scalar, dict, list, str, regex, default None Value to replace any values matching to_replace with
   2. inplace : bool, default False
    If True, performs operation inplace and returns None.
limit : int, default None
    Maximum size gap to forward or backward fill.

>>> df.replace({'A': 0, 'B': 5}, 100)
        A    B  C
0  100  100  a
1    1    6  b
2    2    7  c
3    3    8  d
4    4    9  e
```

`Parameters`

- value : scalar, dict, list, str, regex, default None
  - Value to replace any values matching to_replace with.
- inplace : bool, default False
  - If True, performs operation inplace and returns None.
- limit : int, default None
  - Maximum size gap to forward or backward fill.
- regex : bool or same types as to_replace, default False
  - Whether to interpret to_replace and/or value as regular expressions.
- method : {'pad', 'ffill', 'bfill', None}
  - The method to use when for replacement, when to_replace is a scalar, list or tuple and value is None.
- Returns => DataFrame
  - Object after replacement.

```py
def _convert_to_text(link):
    parsed = urlparse.urlparse(link.url)
    site = parsed[1]
    rest = ' '.join(re.split(r'[/.-_]', parsed[2]))
    data = '%s %s %s user*%s topic:%s %s' % (site, rest, link.text, link.user.username, link.topic.name, link.topic.full_name)
    data = data.replace("'", "*")
    data = data.replace("%", "*")
    return data
```

## `method` astype()

1. Cast a pandas object to a specified dtype *dtype*

`Parameters`

- dtype : data type, or dict of column name -> data type
  - Use a numpy.dtype or Python type to cast entire pandas object to the same type.
  - Alternatively, use {col: dtype, ...}, where col is a column label and dtype is a numpy.dtype or Python type to cast one or more of the DataFrame's columns to column-specific types.
- copy : bool, default True => Return a copy when copy=True
- Method Returns => casted : same type as caller

`Examples`

```py
Create a series of dates:

>>> ser_date = pd.Series(pd.date_range('20200101', periods=3))
>>> ser_date
0   2020-01-01
1   2020-01-02
2   2020-01-03
dtype: datetime64[ns]

Create a DataFrame:

>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = pd.DataFrame(data=d)
>>> df.dtypes
col1    int64
col2    int64
dtype: object
Cast all columns to int32:

>>> df.astype('int32').dtypes
col1    int32
col2    int32
dtype: object
```

## method matplotlib.pyplot.subplots()

1. Create a figure and a set of subplots.
   1. This utility wrapper makes it convenient to create common layouts of subplots, including the enclosing figure object, in a single call.

`Examples`

```py
1) matplotlib.pyplot.subplots()

def plotim1(im):
    fig, ax = plt.subplots()
    ax.imshow(im)
    ax.axis('off')
    plt.show()

2) matplotlib.pyplot.subplots(arg1,arg2,figsize=)

def plot_structured_grid(sgr):
    _, ax = plt.subplots(1, 1, figsize=(8, 8))
    sgr.plot(ax=ax)
    return ax

3) matplotlib.pyplot.subplots(figsize=)

def plot_discriminator_score(self, samples):
        fig, axes = plt.subplots(figsize=(10, 10))
        plot_discriminator_score(samples, axes)
        return fig, axes

4) matplotlib.pyplot.subplots(arg1,arg2)

def test_empty_eventplot():
    fig, ax = plt.subplots(1, 1)
    ax.eventplot([[]], colors=[(0.0, 0.0, 0.0, 0.0)])
    plt.draw()

def make_axes(self):
        """Make a set of axes and assign them to the object.
        """
        self.caxes = pl.subplots(len(self.show), len(self.show))
```

## use seaborn and matplotlib to plot data

```py

1) seaborn.pointplot(data=,dodge=,errwidth=,hue=,join=,markers=,palette=,scale=,x=,y=)

def downstream_plot_performance(df):
    print("Plotting...")
    sns.set_theme(style="whitegrid")
    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    xtitle = 'Normalized Performance Metric'

    df = pd.melt(df, ['Model', 'Dataset'], value_vars='metric', value_name=xtitle)
    sns.stripplot(x=xtitle, y="Dataset", hue="Model", data=df, dodge=True, alpha=.25, zorder=1, size=2)
    sns.pointplot(x=xtitle, y="Dataset", hue="Model", data=df, dodge=0.65, join=False,
                  palette="pastel", errwidth=1, markers="d", scale=0.5)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend([handles[labels.index(l) + len(LEGEND_ORDER)] for i, l in enumerate(LEGEND_ORDER)],
              ["({}.) {}".format(i+1, l) for i, l in enumerate(LEGEND_ORDER)], title="Models",
              handletextpad=0, columnspacing=1, fontsize='x-small', loc="best", ncol=1, frameon=True)
    plt.title("Performance Metrics as Multiple of Chance-level By Dataset and Model")
    plt.show()
    print("Done.")

3) seaborn.pointplot(aspect=,ax=,capsize=,color=,conf_lw=,data=,estimator=,x=,y=)

def plot_simulation(s_fname, s_log_to_filter):
    '''
    Plots the data from all trial of a simulation to help navigate between them

    :param s_fname: string. the name of the log of results
    :param s_log_to_filter: string. The log file name used by the simulation
    '''
    # prepare the file to be loaded as a json
    output = StringIO.StringIO()
    output.write('[')
    last_row = None
    for row in open(s_fname):
        if last_row:
            output.write(last_row[:-1] + ',')
        last_row = row
    output.write(last_row[:-1] + ']')
    json_data = json.loads(output.getvalue())
    # load and parse the file
    d_pnl = {}
    d_duration = {}
    d_ntrades = {}

    for row in json_data:
        if row['log_file'] == s_log_to_filter:
            d_pnl[row['trial']] = row['PnL']
            d_duration[row['trial']] = row['Duration']
            d_ntrades[row['trial']] = row['Total_Traded']['total']

    # plot the data
    fig, l_ax = plt.subplots(2, 2, figsize=(8, 6))
    l_ax = list(np.array(l_ax).ravel())
    l_color = sns.color_palette("Set2", 10)

    ###############
    # pnl plot
    ###############
    df_aux = pd.DataFrame(d_pnl)
    df_pnl = df_aux.loc[['last', 'max', 'min'], :]
    df_mdd = df_aux.loc[['MDD'], :]
    df_plot = df_pnl.unstack().reset_index()
    df_plot.columns = ['trial', 'measure', 'pnl']
    df_plot2 = df_plot.copy()
    sns.pointplot(x='trial', y='pnl', data=df_plot, aspect=.75, conf_lw=1,
                  capsize=0.3, estimator=func_estimator, ax=l_ax[0])
    f_avg = df_pnl.loc['last', :].mean()
    f_rows = df_plot[df_plot.measure == 'last'].shape[0] * 1.
    i_hits = ((df_plot[df_plot.measure == 'last'].pnl > 0).sum()/f_rows)*100
    s_txt = 'avg. pnl = {:0.2f} | hits: {:0.1f} %'
    l_ax[0].axhline(xmin=0, xmax=1, y=f_avg, color='black', linestyle='dashed',
                    label=s_txt.format(f_avg, i_hits))
    l_ax[0].set_title('Last/Min/Max PnL', fontsize=12)
    l_ax[0].set_ylabel('PnL')
    l_ax[0].legend(fontsize=8)

    ###############
    # Duration plot
    ###############
    df_aux = pd.DataFrame(d_duration)
    df_aux = df_aux.loc[['avg', 'max', 'min'], :]
    df_plot = df_aux.unstack().reset_index()
    df_plot.columns = ['trial', 'measure', 'duration']
    f_avg = df_aux.loc['avg', :].mean()
    sns.pointplot(x='trial', y='duration', data=df_plot, aspect=.75, conf_lw=1,
                  capsize=0.3, estimator=func_estimator, color=l_color[1],
                  ax=l_ax[3])
    l_ax[3].axhline(xmin=0, xmax=1, y=f_avg, color='black', linestyle='dashed',
                    label='avg. pnl = {:0.2f}'.format(f_avg))
    l_ax[3].set_title('Avg/Min/Max Duration', fontsize=12)
    l_ax[3].set_ylabel('years')
    l_ax[3].legend(fontsize=8)

    ###############
    # Number of operations plot
    ###############
    df_plot = df_mdd.unstack().reset_index()
    df_plot.columns = ['trial', 'measure', 'mdd']
    sns.barplot('trial', y='mdd', color=l_color[7], data=df_plot, ax=l_ax[2])
    l_ax[2].set_title('Maximum Drawdown', fontsize=12)
    l_ax[2].set_ylabel('Loss')

        ###############
    # Number of operations plot
    ###############
    df_plot = df_mdd.unstack().reset_index()
    df_plot.columns = ['trial', 'measure', 'mdd']
    sns.barplot('trial', y='mdd', color=l_color[7], data=df_plot, ax=l_ax[2])
    l_ax[2].set_title('Maximum Drawdown', fontsize=12)
    l_ax[2].set_ylabel('Loss')

    ###############
    # Maximum Drawdown plot
    ###############
    df_plot = pd.DataFrame(pd.Series(d_ntrades))
    df_plot /= 5
    df_plot = df_plot.astype(int)
    df_plot = df_plot.unstack().reset_index()
    df_plot.columns = ['aux', 'trial', 'qty']
    sns.barplot('trial', y='qty', color=l_color[7], data=df_plot, ax=l_ax[1])
    l_ax[1].set_title('Number of Operations', fontsize=12)
    l_ax[1].set_ylabel('Qty')

    s_title = u'Agent: {}    |    File: {}'.format(json_data[0]['Agent'],
                                                   json_data[0]['log_file'])
    fig.suptitle(s_title, y=1.03, fontsize=15)
    fig.tight_layout()

    return df_plot2

```

## Analyze Data

### (method) corr: (method: _str = ..., min_periods: int = ...) -> DataFrame

1. Compute pairwise correlation of columns, excluding NA/null values.

`Parameters`

- method : {'pearson', 'kendall', 'spearman'} or callable
  - Method of correlation:
    - pearson : standard correlation coefficient
    - kendall : Kendall Tau correlation coefficient
    - spearman : Spearman rank correlation
    - callable: callable with input two 1d ndarrays and returning a float
      - Note that the returned matrix from corr will have 1 along the diagonals and will be symmetric regardless of the callable's behavior. min_periods : int, optional Minimum number of observations required per pair of columns to have a valid result. Currently only available for Pearson and Spearman correlation.
- Returns: DataFrame -> correlation matrix

`Examples`

```py
>>> def histogram_intersection(a, b):
...     v = np.minimum(a, b).sum().round(decimals=1)
...     return v
>>> df = pd.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
...                   columns=['dogs', 'cats'])
>>> df.corr(method=histogram_intersection)
      dogs  cats
dogs   1.0   0.3
cats   0.3   1.0
```

## (method) abs()

1. (method) abs: () -> DataFrame
   1. Return a Series/DataFrame with absolute numeric value of each element.
   2. This function only applies to elements that are all numeric.
2. Returns: abs => Series/DataFrame containing the absolute value of each element.

`Examples`

```py
For complex inputs, 1.2 + 1j, the absolute value is \sqrt{ a^2 + b^2 }.

# Examples: Absolute numeric values in a Series.

>>> s = pd.Series([-1.10, 2, -3.33, 4])
>>> s.abs()
0    1.10
1    2.00
2    3.33
3    4.00
dtype: float64
# Absolute numeric values in a Series with complex numbers.

>>> s = pd.Series([1.2 + 1j])
>>> s.abs()
0    1.56205
dtype: float64
# Absolute numeric values in a Series with a Timedelta element.

>>> s = pd.Series([pd.Timedelta('1 days')])
>>> s.abs()
0   1 days
dtype: timedelta64[ns]
Select rows with data closest to certain value using argsort (from
StackOverflow <https://stackoverflow.com/a/17758115>__).

>>> df = pd.DataFrame({
...     'a': [4, 5, 6, 7],
...     'b': [10, 20, 30, 40],
...     'c': [100, 50, -30, -50]
... })
>>> df
     a    b    c
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50
>>> df.loc[(df.c - 43).abs().argsort()]
     a    b    c
1    5   20   50
0    4   10  100
2    6   30  -30
3    7   40  -50
```

### Options

`maxAge`: defaulting to 0 (can be string converted by ms)
`root`: root directory for relative filenames
`headers`: object of headers to serve with file

1. can auto set Content-Type response header field. callback fn(err) is invoked when tran. is complete or error occurs.
2. Can check res.headersSent to attempt responding; since the header and some data could've already been tran.

`dotfiles`: serve dotfiles, defaulting to false; can be "allow" to send them
`Other`: options are passed along to send.

#### Examples

> Using res.sendFile() as an alt for static() middleware for dynamic situations (uses the same code underneath and supports HTTP cache, etc.)

```py
app.get('/user/:uid/photos/:file', function(req, res){
  var uid = req.params.uid
    , file = req.params.file;

  req.user.mayViewFilesFrom(uid, function(yes){
    if (yes) {
      res.sendFile('/uploads/' + uid + '/' + file);
    } else {
      res.send(403, 'Sorry! you cant see that.');
    }
  });
});
@api — public
```

## Initial env setup for PostgreSQL DB

```sh
python3 -m venv .venv

source /home/ib-ub/dedubu/.venv/bin/activate

apt install postgresql postgresql-contrib

pg_ctlcluster 12 main start # used to start server

sudo -u postgres psq
sudo service postgresql  <status | start | stop>
# \q or ctrl D to exit psql shell
```

## Server Info

Ver Cluster Port Status Owner    Data directory              Log file
12  main    5432 down   postgres /var/lib/postgresql/12/main /var/log/postgresql/postgresql-12-main.log

[PostgreSQL][PSQL]

[PSQL]: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database
