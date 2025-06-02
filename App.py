import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

st.title("Simulação de Fila M/M/c - Restaurante Universitário")

uploaded_file = st.file_uploader("Faça upload do arquivo CSV com colunas 'interarrival_time' e 'service_time'", type=["csv"])

c = st.number_input("Número de servidores (c)", min_value=1, max_value=10, value=3, step=1)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
    else:
        if 'interarrival_time' not in df.columns or 'service_time' not in df.columns:
            st.error("CSV deve conter colunas 'interarrival_time' e 'service_time'")
        else:
            interarrival_times = df['interarrival_time'].values
            service_times = df['service_time'].values
            
            # Proteção contra zeros
            if np.any(interarrival_times <= 0) or np.any(service_times <= 0):
                st.error("Todos os tempos devem ser maiores que zero.")
            else:
                arrival_times = np.cumsum(interarrival_times)
                n = len(arrival_times)
                start_service = np.zeros(n)
                end_service = np.zeros(n)
                servers_free_at = np.zeros(c)

                for i in range(n):
                    arrival = arrival_times[i]
                    service = service_times[i]
                    server_index = np.argmin(servers_free_at)
                    start = max(arrival, servers_free_at[server_index])
                    servers_free_at[server_index] = start + service
                    start_service[i] = start
                    end_service[i] = start + service

                Wq = start_service - arrival_times
                W = end_service - arrival_times

                lam = 1 / np.mean(interarrival_times)
                mu = 1 / np.mean(service_times)
                rho = lam / (c * mu)

                if rho >= 1:
                    st.warning("O sistema está instável (ρ >= 1). Os cálculos podem não ser válidos.")
                
                def calc_p0(lam, mu, c, rho):
                    sum_terms = sum(((lam/mu)**n) / math.factorial(n) for n in range(c))
                    if rho == 1:
                        return 0  # evitar divisão por zero
                    last_term = ((lam/mu)**c) / (math.factorial(c) * (1 - rho))
                    return 1 / (sum_terms + last_term)

                P0 = calc_p0(lam, mu, c, rho) if rho < 1 else 0
                P_wait = (((lam/mu)**c) / math.factorial(c)) * (rho / (1 - rho)) * P0 if rho < 1 else 1

                Lq = np.mean(Wq) / np.mean(service_times)
                L = np.mean(W) / np.mean(service_times)

                st.subheader("Métricas calculadas")
                st.write(f"P₀ (Sistema vazio): {P0:.4f}")
                st.write(f"Probabilidade de espera: {P_wait:.4f}")
                st.write(f"Número médio na fila (Lq): {Lq:.4f}")
                st.write(f"Tempo médio de espera na fila (Wq): {np.mean(Wq):.4f}")
                st.write(f"Tempo médio no sistema (W): {np.mean(W):.4f}")
                st.write(f"Número médio no sistema (L): {L:.4f}")

                st.subheader("Visualizações")

                # Gráfico 1: Tempo de espera
                fig1, ax1 = plt.subplots()
                ax1.plot(range(n), Wq, marker='o')
                ax1.set_title('Tempo de espera na fila por cliente')
                ax1.set_xlabel('Cliente')
                ax1.set_ylabel('Tempo de espera')
                ax1.grid(True)
                st.pyplot(fig1)
                plt.close(fig1)

                # Gráfico 2: Tamanho da fila
                time_points = np.linspace(0, max(end_service), 1000)
                queue_sizes = [np.sum((arrival_times <= t) & (start_service > t)) for t in time_points]

                fig2, ax2 = plt.subplots()
                ax2.plot(time_points, queue_sizes)
                ax2.set_title('Tamanho da fila ao longo do tempo')
                ax2.set_xlabel('Tempo')
                ax2.set_ylabel('Número na fila')
                ax2.grid(True)
                st.pyplot(fig2)
                plt.close(fig2)

                # Gráfico 3: Ocupação dos servidores
                servers_busy = [np.sum((start_service <= t) & (end_service > t)) for t in time_points]

                fig3, ax3 = plt.subplots()
                ax3.plot(time_points, servers_busy)
                ax3.set_title('Ocupação dos servidores ao longo do tempo')
                ax3.set_xlabel('Tempo')
                ax3.set_ylabel('Servidores ocupados')
                ax3.grid(True)
                st.pyplot(fig3)
                plt.close(fig3)

                # Exportar resultados
                results = pd.DataFrame({
                    'arrival_time': arrival_times,
                    'start_service': start_service,
                    'end_service': end_service,
                    'wait_time': Wq,
                    'total_time': W
                })
                csv = results.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download resultados da simulação (CSV)",
                    data=csv,
                    file_name='resultados_simulacao.csv',
                    mime='text/csv',
                )
