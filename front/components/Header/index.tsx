import styles from './styles.module.scss'
import { ActiveLink } from '../ActiveLink'
import Link from 'next/link'
import { SignInButton } from '../SignInButton'
import { useSession } from 'next-auth/client'

export function Header() {
	const [session] = useSession()

	const dashboard = session ? (
		<ActiveLink activeClassName={styles.active} href="/dashboard">
			<a>Dashboard</a>
		</ActiveLink>
	) : null

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

					{dashboard}
				</nav>
				<SignInButton />
			</div>
		</header>
	)
}
