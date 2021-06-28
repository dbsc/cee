import styles from './styles.module.scss'

export function Numeros() {
	return (
		<div className={styles.container}>
			<div className={styles.Faixa}></div>
			<h1 className={styles.title}>
				Nosso Trabalho em Números
			</h1>
			<div className={styles.content}>
				<div className={styles.numbers}>
					<div className={styles.left}>
						<div className={`${styles.box} ${styles.a}`}>
							<h1>+550 de Oportunidades Divulgadas</h1>
							<p>
								através de nossos meios de divulgação, que incluem grupos de facebook e mailing, a mais de
							</p>
							<h1>+1.000 Alunos e Ex-alunos</h1>
						</div>
						<div className={`${styles.box} ${styles.b}`}>
							<h1>Mais que Dobramos</h1>
							<p>
								o número de empresas com programas de estágio adequados para os alunos da instituição em 2016,
							</p>
							<h1>Aumentando a Adesão e Melhorando</h1>
							<p>
								a experiência dos alunos e das empresas.
							</p>
						</div>
						<div className={`${styles.box} ${styles.c}`}>
							<h1>14 Alunos do Primeiro Ano</h1>
							<p>
								realizaram estágios de férias em 2017, somados a muitos outros alunos 
								em outras etapas da graduação.
							</p>
						</div>
					</div>
					<div className={styles.right}>
						<div className={`${styles.box} ${styles.d}`}>
							<h1>428 Alunos do ITA</h1>
							<p>
								participaram da VI Feira de Carreiras do ITA em 2019, que contou com
							</p>
							<h1>27 Empresas e 150 Expositores</h1>
						</div>
						<div className={`${styles.box} ${styles.e}`}>
							<h1>73 Eventos</h1>
							<p>
							realizados em 2019, incluindo palestras, visitas, hackathons, treinamentos, 
							Feira de Carreiras entre outros, sendo realizados no Campus do ITA e em SP Capital.
							</p>
						</div>
						<div className={`${styles.box} ${styles.f}`}>
							<h1>58 Empresas</h1>
							<p>
							participaram de eventos promovidos pela CEE em 2019, recebendo todo o suporte 
							necessário para agendamento, locação e divulgação.
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	)
}
