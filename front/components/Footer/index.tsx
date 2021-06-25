import styles from './styles.module.scss'
import { FiPhone, FiMapPin, FiMail, FiLinkedin, FiFacebook, FiInstagram } from 'react-icons/fi'

export function Footer() {
	return (
		<footer className={styles.container}>
			<div className={styles.content}>
				<div className={styles.logo}>
					<img src="/logos/logo_white_CEE.svg" alt="Logo CEE" />
					<p>
						Uma iniciativa de alunos do ITA para
						<br />
						toda a comunidade iteana!
					</p>
				</div>
				<div className={styles.contato}>
					<h1>Contato</h1>
					<div className={styles.telefone}>
						<FiPhone />
						<p>(12) 98125 3244</p>
					</div>
					<div className={styles.endereco}>
						<FiMapPin />
						<p>Rua H8A, 144, Campus do CTA São José dos Campos SP, 12228-460</p>
					</div>
					<a className={styles.email} href="mailto:contato@ceeita.com" >
						<FiMail />
						<p>contato@ceeita.com</p>
					</a>
				</div>
				<div className={styles.redesSociais}>
					<h1>Nossas Redes</h1>
					<div className={styles.icons}>
						<a href="https://www.instagram.com/cee_ita/" target="blank"><FiInstagram /></a>
						<a href="https://www.facebook.com/estagiosita/" target="blank"><FiFacebook /></a>
						<a href="https://www.linkedin.com/company/cee-ita/" target="blank"><FiLinkedin /></a>
					</div>
					<a className={styles.button} href="/">
						Fazer Login
					</a>
				</div>
			</div>
			<div className={styles.copyright}>
				<p>Copyright © 2021 CEE - Todos os direitos reservados</p>
			</div>
		</footer>
	)
}
