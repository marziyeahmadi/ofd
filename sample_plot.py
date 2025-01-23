import numpy as np
import plotly.graph_objects as go

fig = go.Figure()

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='sin(x)'))

fig.update_layout(
    title='Somthing cool',
    xaxis_title='x',
    yaxis_title='sin(x)',
)

fig.show()