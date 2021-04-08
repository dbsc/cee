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
						<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia cupiditate vitae</p>
					</div>
					<div>
						<h1>Eventos Semanais</h1>
						<img src="/icones/eventos.svg" alt="Eventos Semanais" />
						<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia cupiditate vitae</p>
					</div>
					<div>
						<h1>Feira de Carreiras</h1>
						<img src="/icones/carreira.svg" alt="Feira de Carreiras" />
						<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia cupiditate vitae</p>
					</div>
					<div>
						<h1>Estruturação de Estágios </h1>
						<img src="/icones/estagio.svg" alt="Estruturação de Estágios " />
						<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia cupiditate vitae</p>
					</div>
				</div>
			</div>
		</div>
	)
}
