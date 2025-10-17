!pip install yfinance
!pip install bs4
!pip install nbformat
!pip install --upgrade plotly
----- # these 5 dashes seperates cells
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
----- # From line 1 to 4, its the 1st cell, then from line 6 to line 11, its the 2nd cell, and so on.
import plotly.io as pio
pio.renderers.default = "iframe"
----- # the 1st cell of question 2  of my project is from line 42 to line 44, and when i executed that cell, i got an error, i have copy-pasted the error, starting from line 46
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))
----- # I manually copy pasted some of the cells, beacuse i couldnt upload my file on my github repo, i tried to do it, but github couldnt open it, its showing "invalid Notebook"
tesla = yf.Ticker("TSLA")
-----
tesla_data = tesla.history(period="max")
-----
tesla_data.reset_index(inplace=True)
tesla_data.head()
-----
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
html_data = response.text
----- # so from line 46 till the end, that was the error i got, please sir/mam, look into it and suggest what should i do
OSError                                   Traceback (most recent call last)
File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/urllib3/connectionpool.py:711, in HTTPConnectionPool.urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
    710 if is_new_proxy_conn and http_tunnel_required:
--> 711     self._prepare_proxy(conn)
    713 # Make the request on the httplib connection object.

File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/urllib3/connectionpool.py:1007, in HTTPSConnectionPool._prepare_proxy(self, conn)
   1005     conn.tls_in_tls_required = True
-> 1007 conn.connect()

File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/urllib3/connection.py:374, in HTTPSConnection.connect(self)
    372 # Calls self._set_hostport(), so self.host is
    373 # self._tunnel_host below.
--> 374 self._tunnel()
    375 # Mark this connection as not reusable

File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/http/client.py:926, in HTTPConnection._tunnel(self)
    925     self.close()
--> 926     raise OSError(f"Tunnel connection failed: {code} {message.strip()}")
    927 while True:

OSError: Tunnel connection failed: 403 Forbidden

During handling of the above exception, another exception occurred:

MaxRetryError                             Traceback (most recent call last)
File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/requests/adapters.py:486, in HTTPAdapter.send(self, request, stream, timeout, verify, cert, proxies)
    485 try:
--> 486     resp = conn.urlopen(
    487         method=request.method,
    488         url=url,
    489         body=request.body,
    490         headers=request.headers,
    491         redirect=False,
    492         assert_same_host=False,
    493         preload_content=False,
    494         decode_content=False,
    495         retries=self.max_retries,
    496         timeout=timeout,
    497         chunked=chunked,
    498     )
    500 except (ProtocolError, OSError) as err:

File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/urllib3/connectionpool.py:798, in HTTPConnectionPool.urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
    796     e = ProtocolError("Connection aborted.", e)
--> 798 retries = retries.increment(
    799     method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
    800 )
    801 retries.sleep()

File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/urllib3/util/retry.py:592, in Retry.increment(self, method, url, response, error, _pool, _stacktrace)
    591 if new_retry.is_exhausted():
--> 592     raise MaxRetryError(_pool, url, error or ResponseError(cause))
    594 log.debug("Incremented Retry for (url='%s'): %r", url, new_retry)

MaxRetryError: HTTPSConnectionPool(host='cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud', port=443): Max retries exceeded with url: /IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm (Caused by ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 403 Forbidden')))

During handling of the above exception, another exception occurred:

ProxyError                                Traceback (most recent call last)
Cell In[5], line 2
      1 url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
----> 2 response = requests.get(url)
      3 html_data = response.text

File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/requests/api.py:73, in get(url, params, **kwargs)
     62 def get(url, params=None, **kwargs):
     63     r"""Sends a GET request.
     64 
     65     :param url: URL for the new :class:`Request` object.
   (...)
     70     :rtype: requests.Response
     71     """
---> 73     return request("get", url, params=params, **kwargs)

File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/requests/api.py:59, in request(method, url, **kwargs)
     55 # By using the 'with' statement we are sure the session is closed, thus we
     56 # avoid leaving sockets open which can trigger a ResourceWarning in some
     57 # cases, and look like a memory leak in others.
     58 with sessions.Session() as session:
---> 59     return session.request(method=method, url=url, **kwargs)

File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/requests/sessions.py:589, in Session.request(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
    584 send_kwargs = {
    585     "timeout": timeout,
    586     "allow_redirects": allow_redirects,
    587 }
    588 send_kwargs.update(settings)
--> 589 resp = self.send(prep, **send_kwargs)
    591 return resp

File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/requests/sessions.py:703, in Session.send(self, request, **kwargs)
    700 start = preferred_clock()
    702 # Send the request
--> 703 r = adapter.send(request, **kwargs)
    705 # Total elapsed time of the request (approximately)
    706 elapsed = preferred_clock() - start

File /opt/conda/envs/anaconda-panel-2023.05-py310/lib/python3.11/site-packages/requests/adapters.py:513, in HTTPAdapter.send(self, request, stream, timeout, verify, cert, proxies)
    510     raise RetryError(e, request=request)
    512 if isinstance(e.reason, _ProxyError):
--> 513     raise ProxyError(e, request=request)
    515 if isinstance(e.reason, _SSLError):
    516     # This branch is for urllib3 v1.22 and later.
    517     raise SSLError(e, request=request)

ProxyError: HTTPSConnectionPool(host='cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud', port=443): Max retries exceeded with url: /IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm (Caused by ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 403 Forbidden')))









