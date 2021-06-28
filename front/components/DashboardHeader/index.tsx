import styles from './styles.module.scss'
import { ActiveLink } from '../ActiveLink'
import Link from 'next/link'
import { SignInButton } from '../SignInButton'

export function DashBoardHeader() {
	return (
		<header className={styles.container}>
			<div className={styles.content}>
				<Link href="/">
					<img src="/logos/logo_white_text.svg" alt="CEE" />
				</Link>
				<nav>
					<ActiveLink activeClassName={styles.active} href="/dashboard">
						<a>Home</a>
					</ActiveLink>
					<ActiveLink activeClassName={styles.active} href="/vagas">
						<a>Vagas</a>
					</ActiveLink>
					<ActiveLink activeClassName={styles.active} href="/eventos">
						<a>Eventos</a>
					</ActiveLink>
				</nav>
				<SignInButton />
			</div>
		</header>
	)
}
