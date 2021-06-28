import styles from './styles.module.scss'

export function Servicos() {
	return (
		<div className={styles.container}>
			<div className={styles.content}>
				<h1 className={styles.title}>
					Nossos <br />
					Serviços
				</h1>
				<div className={styles.cards}>
					<div>
						<h1>Divulgação de Oportunidades</h1>
						<img src="/icones/oportunidades.svg" alt="Divulgação de Oportunidades" />
						<p>Divulgamos todo tipo de oportunidade interessante para a comunidade iteana</p>
					</div>
					<div>
						<h1>Eventos Semanais</h1>
						<img src="/icones/eventos.svg" alt="Eventos Semanais" />
						<p>Organizamos eventos e treinamentos toda semana com empresas parceiras</p>
					</div>
					<div>
						<h1>Feira de Carreiras</h1>
						<img src="/icones/carreira.svg" alt="Feira de Carreiras" />
						<p>Organizamos o maior evento anual do ITA reunindo muitas empresas de interesse da comunidade</p>
					</div>
					<div>
						<h1>Estruturação de Estágios </h1>
						<img src="/icones/estagio.svg" alt="Estruturação de Estágios " />
						<p>Auxiliamos na divulgação e aplicação de processos seletivos de estágios</p>
					</div>
				</div>
			</div>
		</div>
	)
}
