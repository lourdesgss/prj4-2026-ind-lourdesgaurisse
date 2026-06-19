from nicegui import ui
from NeuralPredictor import HardwarePredictor
import pandas as pd

# ── Theme injection ───────────────────────────────────────────────────────────
ui.add_head_html("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&family=Syne:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg:        #070c18;
    --surface:   #0d1628;
    --surface2:  #111e36;
    --border:    #1a3050;
    --accent:    #3b82f6;
    --accent-lo: #1d4ed8;
    --text:      #dbeafe;
    --muted:     #6b8aaa;
    --radius:    12px;
  }

  body, .q-page, .nicegui-content {
    background: var(--bg) !important;
    font-family: 'DM Mono', monospace !important;
    color: var(--text) !important;
  }

  /* ── scrollbar ── */
  ::-webkit-scrollbar { width: 6px; height: 6px; }
  ::-webkit-scrollbar-track { background: var(--surface); }
  ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

  /* ── card ── */
  .np-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 24px;
  }

  /* ── label overrides ── */
  .np-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 4px;
  }

  .np-heading {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.01em;
  }

  .np-section {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    color: var(--text);
  }

  /* ── inputs ── */
  .q-field__control {
    background: var(--surface2) !important;
    border-radius: 8px !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
  }
  .q-field__control:hover { border-color: var(--accent) !important; }
  .q-field--focused .q-field__control { border-color: var(--accent) !important; box-shadow: 0 0 0 3px rgba(59,130,246,.15) !important; }
  .q-field__native, .q-field__input { color: var(--text) !important; font-family: 'DM Mono', monospace !important; }
  .q-field__label { color: var(--muted) !important; font-family: 'DM Mono', monospace !important; font-size: 0.8rem !important; }
  .q-field__bottom { display: none; }
  .q-field--outlined .q-field__control:before { border: none !important; }
  .q-field--outlined .q-field__control:after { border: none !important; }

  /* select dropdown */
  .q-menu { background: var(--surface) !important; border: 1px solid var(--border) !important; border-radius: 8px !important; }
  .q-item { color: var(--text) !important; }
  .q-item:hover { background: var(--surface2) !important; }
  .q-item--active { color: var(--accent) !important; background: rgba(59,130,246,.1) !important; }

  /* ── predict button ── */
  .np-btn .q-btn {
    background: var(--accent) !important;
    color: #fff !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.05em;
    padding: 10px 28px !important;
    transition: background 0.2s, box-shadow 0.2s;
    width: 100%;
  }
  .np-btn .q-btn:hover {
    background: var(--accent-lo) !important;
    box-shadow: 0 0 20px rgba(59,130,246,.35) !important;
  }

  /* ── download button ── */
  .np-dl .q-btn {
    background: transparent !important;
    color: var(--accent) !important;
    border: 1px solid var(--accent) !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    padding: 7px 20px !important;
    transition: background 0.2s;
  }
  .np-dl .q-btn:hover { background: rgba(59,130,246,.1) !important; }

  /* ── tabs ── */
  .q-tabs { background: transparent !important; border-bottom: 1px solid var(--border); }
  .q-tab { color: var(--muted) !important; font-family: 'DM Mono', monospace !important; font-size: 0.78rem !important; }
  .q-tab--active { color: var(--accent) !important; }
  .q-tab-indicator { background: var(--accent) !important; }
  .q-tab-panels { background: transparent !important; }
  .q-tab-panel { padding: 16px 0 !important; }

  /* ── separator ── */
  .q-separator { background: var(--border) !important; margin: 20px 0 !important; }

  /* ── echart backgrounds ── */
  .np-chart-wrap {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 8px;
  }
</style>
""")

# ── State ─────────────────────────────────────────────────────────────────────
predictor = HardwarePredictor()

# ── Layout ───────────────────────────────────────────────────────────────────
with ui.row().style('width:100%;min-height:100vh;align-items:flex-start;gap:24px;padding:32px;box-sizing:border-box;background:var(--bg)'):

    # ── LEFT: Parameters ────────────────────────────────────────────────────
    with ui.column().style('width:260px;flex-shrink:0;gap:0'):

        # wordmark
        with ui.column().style('gap:2px;margin-bottom:28px'):
            ui.label('NEURAL').classes('np-title').style('margin-bottom:0')
            ui.label('Predictor').classes('np-heading')

        with ui.element('div').classes('np-card'):

            ui.label('Parameters').classes('np-title').style('margin-bottom:16px')

            with ui.column().style('gap:14px;width:100%'):
                v_input   = ui.number('Voltage  V',    value=25,   format='%.2f').style('width:100%').props('outlined dense')
                fr_input  = ui.number('F_r',           value=1.2,  format='%.3f').style('width:100%').props('outlined dense')
                dt2_input = ui.number('dt2',           value=-300, format='%.0f').style('width:100%').props('outlined dense')
                color_input = ui.select([1, 2, 3, 4], value=1, label='Color').style('width:100%').props('outlined dense')

            ui.element('div').style('height:20px')

            with ui.element('div').classes('np-btn'):
                ui.button('Run Prediction', on_click=lambda: run_prediction())

    # ── RIGHT: Results ──────────────────────────────────────────────────────
    results_column = ui.column().style('flex:1;min-width:0;gap:0')


# ── Prediction logic ─────────────────────────────────────────────────────────
def run_prediction():
    results_column.clear()

    df, predictions = predictor.predict(
        V=v_input.value,
        F_r=fr_input.value,
        dt2=dt2_input.value,
        color=int(color_input.value)
    )

    chunks = predictor.predict_chunks(
        V=v_input.value,
        F_r=fr_input.value,
        dt2=dt2_input.value,
        color=int(color_input.value)
    )

    save_array = predictor.save(df, predictions)

    columns = ["Color$", "V", "F_r", "dt2", "Coverage#"]
    columns.extend([f'Nozzle_{i+1}' for i in range(33600)])
    export_df = pd.DataFrame(save_array, columns=columns)
    filename = "prediction.csv"
    export_df.to_csv(filename, index=False)

    with results_column:

        # ── header row ──
        with ui.row().style('align-items:center;justify-content:space-between;margin-bottom:20px;width:100%'):
            ui.label('Results').classes('np-heading')
            with ui.element('div').classes('np-dl'):
                ui.button('↓ Export CSV', on_click=lambda: ui.download(filename))

        # ── per-chip tabs ──
        with ui.element('div').classes('np-card').style('width:100%;box-sizing:border-box'):

            ui.label('Per-Chip Profiles').classes('np-section').style('margin-bottom:16px')

            tabs   = ui.tabs().props('dense')
            panels = ui.tab_panels(tabs)

            with tabs:
                for cov in range(6):
                    ui.tab(f'Coverage {cov + 1}')

            with panels:
                for cov in range(6):
                    with ui.tab_panel(f'Coverage {cov + 1}'):
                        with ui.grid(columns=3).style('gap:12px;width:100%'):
                            for idx, snippet in enumerate(chunks[cov]):
                                y  = snippet.tolist()
                                xy = list(zip(range(len(y)), y))
                                with ui.element('div').classes('np-chart-wrap'):
                                    ui.echart({
                                        'backgroundColor': 'transparent',
                                        'title': {
                                            'text': f'Chip {idx + 1}',
                                            'textStyle': {'color': '#dbeafe', 'fontSize': 11, 'fontWeight': '500', 'fontFamily': 'DM Mono'},
                                            'top': 4, 'left': 8
                                        },
                                        'grid': {'top': 36, 'right': 8, 'bottom': 24, 'left': 36},
                                        'xAxis': {'type': 'value', 'min': 0, 'max': 1120, 'interval': 280,
                                                  'axisLabel': {'color': '#6b8aaa', 'fontSize': 9, 'fontFamily': 'DM Mono'},
                                                  'axisLine': {'lineStyle': {'color': '#1a3050'}},
                                                  'splitLine': {'lineStyle': {'color': '#111e36'}}},
                                        'yAxis': {'type': 'value',
                                                  'axisLabel': {'color': '#6b8aaa', 'fontSize': 9, 'fontFamily': 'DM Mono'},
                                                  'axisLine': {'lineStyle': {'color': '#1a3050'}},
                                                  'splitLine': {'lineStyle': {'color': '#111e36'}}},
                                        'series': [{'type': 'line', 'showSymbol': False,
                                                    'data': xy,
                                                    'lineStyle': {'color': '#3b82f6', 'width': 1.5},
                                                    'areaStyle': {'color': {'type': 'linear', 'x': 0, 'y': 0, 'x2': 0, 'y2': 1,
                                                                            'colorStops': [{'offset': 0, 'color': 'rgba(59,130,246,.18)'},
                                                                                           {'offset': 1, 'color': 'rgba(59,130,246,0)'}]}}}]
                                    }).style('width:370px;height:220px')

        ui.element('div').style('height:24px')

        # ── full prediction ──
        with ui.element('div').classes('np-card').style('width:100%;box-sizing:border-box'):

            ui.label('Full Prediction  —  33 600 nozzles').classes('np-section').style('margin-bottom:16px')

            for cov in range(6):
                y  = predictions[cov].tolist()
                xy = list(zip(range(predictions.shape[1]), y))

                with ui.element('div').style('margin-bottom:16px'):
                    ui.label(f'Coverage {cov + 1}').style(
                        'font-family:"DM Mono",monospace;font-size:0.72rem;'
                        'color:var(--muted);text-transform:uppercase;letter-spacing:.1em;margin-bottom:6px'
                    )
                    with ui.element('div').classes('np-chart-wrap'):
                        ui.echart({
                            'backgroundColor': 'transparent',
                            'dataZoom': [{'type': 'inside'}, {'type': 'slider',
                                          'height': 18,
                                          'handleStyle': {'color': '#3b82f6'},
                                          'fillerColor': 'rgba(59,130,246,.12)',
                                          'borderColor': '#1a3050',
                                          'textStyle': {'color': '#6b8aaa', 'fontSize': 9}}],
                            'grid': {'top': 16, 'right': 16, 'bottom': 48, 'left': 48},
                            'xAxis': {'type': 'value', 'min': 0, 'max': 33600, 'interval': 3360,
                                      'axisLabel': {'color': '#6b8aaa', 'fontSize': 9, 'fontFamily': 'DM Mono'},
                                      'axisLine': {'lineStyle': {'color': '#1a3050'}},
                                      'splitLine': {'lineStyle': {'color': '#111e36', 'type': 'dashed'}}},
                            'yAxis': {'type': 'value',
                                      'axisLabel': {'color': '#6b8aaa', 'fontSize': 9, 'fontFamily': 'DM Mono'},
                                      'axisLine': {'lineStyle': {'color': '#1a3050'}},
                                      'splitLine': {'lineStyle': {'color': '#111e36', 'type': 'dashed'}}},
                            'series': [{'type': 'line', 'showSymbol': False,
                                        'sampling': 'lttb',
                                        'data': xy,
                                        'lineStyle': {'color': '#3b82f6', 'width': 1.5},
                                        'areaStyle': {'color': {'type': 'linear', 'x': 0, 'y': 0, 'x2': 0, 'y2': 1,
                                                                'colorStops': [{'offset': 0, 'color': 'rgba(59,130,246,.2)'},
                                                                               {'offset': 1, 'color': 'rgba(59,130,246,0)'}]}}}]
                        }).style('width:100%;height:300px')


ui.run()