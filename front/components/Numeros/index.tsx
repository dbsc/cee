import styles from './styles.module.scss'

export function Numeros() {
	return (
		<div className={styles.container}>
			<div className={styles.content}>
				<h1 className={styles.title}>
					Nosso Trabalho em <br />
					Números
				</h1>

				<div className={styles.numbers}>
					<div className={styles.left}>
						<div className={`${styles.box} ${styles.a}`}>
							<h1>+550 Oportunidades</h1>
							<p>
								Foram divulgadas através dos nossos meios de divulgação, que incluem mailing e grupo
								do facebook dedicado à vagas com +1000 iteanos.
							</p>
						</div>
						<div className={`${styles.box} ${styles.b}`}>
							<h1>73 Eventos</h1>
							<p>
								Foram realizados em 2019. Incluindo palestras, visitas, hackathons, treinamentos,
								Feira de Carreiras entre outros. Sendo realizados no Campus do ITA e em SP Capital.
							</p>
						</div>
					</div>
					<div className={styles.right}>
						<div className={`${styles.box} ${styles.c}`}>
							<h1>428 Alunos do ITA</h1>
							<p>
								Empresas participaram de eventos organizados pela CEE em 2019. Recebendo todo
								suporte para agendamento (levando em conta o calendário do ITA), locação do espaço,
								divulgação, coffe-break e preparativos para o dia.
							</p>
						</div>
						<div className={`${styles.box} ${styles.d}`}>
							<h1>58 Empresas</h1>
							<p>
								Participaram da VI Feira de Carreiras do ITA em 2019. O evento contou com 27
								empresas e 150 expositores, além de alunos de outras faculdades de excelência.
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	)
}
