import styles from './styles.module.scss'
import { ActiveLink } from '../ActiveLink'
import Link from 'next/link'
import { SignInButton } from '../SignInButton'

export function Header() {
	return (
		<header className={styles.container}>
			<div className={styles.content}>
				<Link href="/">
					<img src="/logos/logo_white_text.svg" alt="CEE" />
				</Link>
				<nav>
					<ActiveLink activeClassName={styles.active} href="/">
						<a>Home</a>
					</ActiveLink>
					<ActiveLink activeClassName={styles.active} href="/quem-somos">
						<a>Quem Somos</a>
					</ActiveLink>
					<ActiveLink activeClassName={styles.active} href="https://forms.gle/V3oNNjSKr5ZnQtQT8">
						<a target="blank ">Divulgar Vaga no ITA </a>
					</ActiveLink>
					<ActiveLink activeClassName={styles.active} href="/contato">
						<a>Contato</a>
					</ActiveLink>
				</nav>
				<SignInButton />
			</div>
		</header>
	)
}
