import styles from './styles.module.scss'
import { FiPhone, FiMapPin, FiMail, FiLinkedin, FiFacebook, FiInstagram } from 'react-icons/fi'

export function FormsRedes(){

    return (
        <div className={styles.container}>
			<div className={styles.content}>
				<div className={styles.contact}>
					<div className={styles.left}>
						<div className={`${styles.box} ${styles.a}`}>
							<h1>Formulário</h1>
							<p>
                                Acesse o formulário de contato pelo <a href="https://forms.gle/V3oNNjSKr5ZnQtQT8" target= "blank">link</a>, para:
							</p>
							<ul>
                                <li>Marcação de Eventos</li>
                                <li>Marcação de Treinamentos</li>
                                <li>Divulgação de Vagas</li>
                                <li>Dúvidas</li>
							</ul>
						</div>
					</div>
					<div className={styles.right}>
						<div className={`${styles.box} ${styles.b}`}>
							<h1>Redes Sociais</h1>
							<p>
                                Caso prefira, nossas redes sociais estão a disposição para esclarecimento de dúvidas.
							</p>
						</div>
						<div className={styles.icons}>
								<FiInstagram />
								<FiFacebook />
								<FiLinkedin />
						</div>
					</div>
				</div>
			</div>
		</div>
    )
}